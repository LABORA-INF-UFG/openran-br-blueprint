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
from ricxappframe.xapp_frame import RMRXapp, rmr
import signal

from .utils.constants import Constants
from .manager import *

from .handler import *
from mdclogpy import Logger
from mdclogpy import Level

import json

class BouncerXapp:

    def __init__(self):
        fake_sdl = getenv("USE_FAKE_SDL", False)
        self._rmr_xapp = RMRXapp(self._default_handler,
                                 config_handler=self._handle_config_change,
                                 rmr_port=4560,
                                 post_init=self._post_init,
                                 use_fake_sdl=False) #use_fake_sdl=bool(fake_sdl))
        
        # Registering callback for active xApp messages
        self._rmr_xapp.register_callback(
            handler=self._handle_act_xapp_msg, message_type=Constants.ACT_XAPP_REQ
        )

        # Registering handlers for signals
        signal.signal(signal.SIGTERM, self._handle_signal)
        signal.signal(signal.SIGQUIT, self._handle_signal)
        signal.signal(signal.SIGINT, self._handle_signal)

    # Executes after _BaseXapp init but before ending the RMRXapp init
    def _post_init(self, rmr_xapp: RMRXapp):
        """
        Function that runs when xapp initialization is complete
        """
        rmr_xapp.logger.set_level(Level.DEBUG)
        rmr_xapp.logger.info("post_init called")

        # Setting up HTTP server
        self.rest_mgr = RestManager(rmr_xapp)
        self.rest_mgr.start_http_server(8080)
        
        # Sending subscription requests for gNBs through SubscriptionManager
        self.sub_mgr = SubscriptionManager(rmr_xapp)
        gnb_list = self.sub_mgr.get_gnb_list() # Getting gNBs
        rmr_xapp.logger.info("Number of gNBs: {}".format(len(gnb_list)))
        id = 54321
        for gnb in gnb_list:
            rmr_xapp.logger.info("Sending subscription request to gNB: {}".format(gnb["inventory_name"]))
            self.sub_mgr.send_subscription_request(xnb_inventory_name=gnb["inventory_name"],subscription_transaction_id=id)
            id += 1

    def _handle_config_change(self, rmr_xapp, config):
        """
        Function that runs at start and on every configuration file change.
        """
        rmr_xapp.logger.info("handle_config_change:: config: {}".format(config))
        rmr_xapp.config = config  # No mutex required due to GIL

    def _handle_act_xapp_msg(self, rmr_xapp:RMRXapp, summary, sbuf):
        """
        Function that responds to active xApp RMR message with an ACK
        """
        rcv_payload = json.loads(summary[rmr.RMR_MS_PAYLOAD])
        rmr_xapp.logger.debug("Received payload = {}".format(rcv_payload))
        count = rmr_xapp.sdl_find_and_get(namespace="ricplt", prefix="bouncer-xapp-ack-count") # Returns {key: value}
        if count is not None:
            rmr_xapp.logger.debug("Get count from SDL: {}".format(count))
        else:
            rmr_xapp.logger.debug("SDL has no value for key: {}".format("bouncer-xapp-ack-count"))
        count = rcv_payload["id"]
        rmr_xapp.logger.debug("Setting on SDL: {}={}".format("bouncer-xapp-ack-count", count))
        rmr_xapp.sdl_set(namespace="ricplt", key="bouncer-xapp-ack-count", value=str(count))
        rmr_xapp.logger.info("Replying ACK {} to active xApp {}".format(rcv_payload["id"], rcv_payload["msg"]))
        payload = json.dumps({"msg":"ACK", "id":rcv_payload["id"]}).encode()
        if not rmr_xapp.rmr_rts(sbuf, new_payload=payload, new_mtype=Constants.REACT_XAPP_ACK):
            rmr_xapp.logger.error("Message could not be replied")

        rmr_xapp.rmr_free(sbuf)
    
    def _handle_signal(self, signum: int, frame):
        """
        Function called when a Kubernetes signal is received that stops the xApp execution.
        """
        self._rmr_xapp.logger.info("Received signal {} to stop the xApp".format(signal.Signals(signum).name))
        self.stop()

    def _default_handler(self, rmr_xapp, summary, sbuf):
        """
        Function that processes messages for which no handler is defined
        """
        rmr_xapp.logger.info("HWXappdefault_handler called for msg type = " +
                                   str(summary[rmr.RMR_MS_MSG_TYPE]))
        rmr_xapp.rmr_free(sbuf)

    def createHandlers(self):
        """
        Function that creates all the handlers for RMR Messages
        """
        HealthCheckHandler(self._rmr_xapp, Constants.RIC_HEALTH_CHECK_REQ)
        A1PolicyHandler(self._rmr_xapp, Constants.A1_POLICY_REQ)
        SubscriptionHandler(self._rmr_xapp,Constants.SUBSCRIPTION_REQ)

    def start(self, thread=False):
        """
        This is a convenience function that allows this xapp to run in Docker
        for "real" (no thread, real SDL), but also easily modified for unit testing
        (e.g., use_fake_sdl). The defaults for this function are for the Dockerized xapp.
        """
        self._rmr_xapp.run(thread, rmr_timeout=5) # Wait 5 second for RMR messages

    def stop(self):
        """
        can only be called if thread=True when started
        """
        self.sub_mgr.delete_subscriptions()
        self.rest_mgr.stop_servers()
        self._rmr_xapp.stop()
