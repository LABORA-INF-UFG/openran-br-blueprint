# ==================================================================================
#
#       Copyright (c) 2020 Samsung Electronics Co., Ltd. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ==================================================================================

from os import getenv
from ricxappframe.xapp_frame import Xapp, rmr
import signal

from .utils.constants import Constants
from .manager import *

from .handler import *
from mdclogpy import Logger
from mdclogpy import Level

from time import sleep
import queue
import json

class ActiveXapp:

    def __init__(self):
        fake_sdl = getenv("USE_FAKE_SDL", False)
        self._xapp = Xapp(self._entrypoint,
                                 #config_handler=self._handle_config_change,
                                 rmr_port=4560,
                                 #post_init=self._post_init,
                                 use_fake_sdl=bool(fake_sdl))
        
        # Creating a dictionary for calling handlers of specific message types
        self._xapp._dispatch = {} 
        self._xapp._dispatch[Constants.REACT_XAPP_ACK] = self._receive_reactive_xapp_ack

        # Handling messages of unregistered types
        self._xapp._default_handler = self._default_handler

        # Flag for shutting down the xApp
        self.shutdown = False

        # Registering handlers for signals
        signal.signal(signal.SIGTERM, self._handle_signal)
        signal.signal(signal.SIGQUIT, self._handle_signal)
        signal.signal(signal.SIGINT, self._handle_signal)

        self._xapp.logger.set_level(Level.DEBUG)
    
    def _handle_signal(self, signum: int, frame):
        """
        Function called when a Kubernetes signal is received that stops the xApp execution.
        """
        self._xapp.logger.info("Received signal {} to stop the xApp".format(signal.Signals(signum).name))
        self.stop()

    def _default_handler(self, xapp, summary, sbuf):
        xapp.logger.info(
            "Received unknow message type {} with payload = {}".format(
                summary[rmr.RMR_MS_MSG_TYPE],
                summary[rmr.RMR_MS_PAYLOAD]
            )
        )
        xapp.rmr_free(sbuf)

    def _receive_reactive_xapp_ack(self, xapp, summary, sbuf):
        rcv_payload = json.loads(summary[rmr.RMR_MS_PAYLOAD])
        xapp.logger.info(
            "Received {} {} from reactive xApp".format(
                rcv_payload["msg"],
                rcv_payload["id"]
            )
        )
        xapp.rmr_free(sbuf) # Need to free the buffer
    
    def _send_active_xapp_req(self, xapp:Xapp, i):
        xapp.logger.info("Sending request {} to reactive xApp".format(i))
        payload = json.dumps({"msg":"Request", "id":i}).encode()
        if not xapp.rmr_send(payload, Constants.ACT_XAPP_REQ):
            xapp.logger.error("Message could not be sent")
        else:
            xapp.logger.debug("Setting on SDL: {}={}".format("active-xapp-send-count", i))

    def _receive_RMR_message(self, xapp:Xapp):
        message_it = self._xapp.rmr_get_messages()
        try:
            while True:
                summary, sbuf = next(message_it)
                self._xapp.logger.info(summary[rmr.RMR_MS_MSG_TYPE])
                func = xapp._dispatch.get(summary[rmr.RMR_MS_MSG_TYPE], None)
                if not func:
                    func = xapp._default_handler
                xapp.logger.debug("invoking msg handler on type {}".format(summary[rmr.RMR_MS_MSG_TYPE]))
                func(xapp, summary, sbuf)
                xapp.rmr_free(sbuf)
        except StopIteration:
            pass
    
    def _generate_managers(self, xapp: Xapp):
        """
        Function that creates all the managers for the xApp
        """
        xapp.logger.info("Generating managers")
        self._subscription_manager = SubscriptionManager(xapp)

    def _entrypoint (self, xapp: Xapp):
        """
        Function that runs in loop from the xApp start until its end
        """
        self._generate_managers(xapp)
        self._subscription_manager.get_gnb_list()

        xapp.logger.info("Running loop")
        i = 0
        while not self.shutdown:
            xapp.logger.debug("Getting gNB SDL information: {}".format(xapp.sdl.find_and_get(ns="ricplt", prefix="GNB")))
            
            count = xapp.sdl.find_and_get(ns="ricplt", prefix="reactive-xapp-ack-count")
            if count is not None:
                xapp.logger.debug("Get count from SDL: {}".format(count))
            else:
                xapp.logger.debug("SDL has no value for key: {}".format("reactive-xapp-ack-count"))
            self._send_active_xapp_req(xapp, i)
            i+=1
            xapp.sdl.set(ns="ricplt", key="active-xapp-send-count", value=str(i))
            sleep(1)
            self._receive_RMR_message(xapp)
        xapp.logger.info("Ended loop")

    def start(self):
        """
        This is a convenience function that allows this xapp to run in Docker
        for "real" (no thread, real SDL), but also easily modified for unit testing
        (e.g., use_fake_sdl). The defaults for this function are for the Dockerized xapp.
        """
        self._xapp.run()

    def stop(self):
        """
        can only be called if thread=True when started
        TODO: could we register a signal handler for Docker SIGTERM that calls this?
        """
        self.shutdown = True
        self._xapp.stop()
