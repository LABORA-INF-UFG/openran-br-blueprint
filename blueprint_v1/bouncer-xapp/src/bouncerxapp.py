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
import time
from binascii import unhexlify, hexlify

from .utils.constants import Constants
from .manager import *
from .handler import *
from .asn1_defs import ASN1_DEFS as e2sm_rc
from mdclogpy import Logger
from mdclogpy import Level

class BouncerXapp:

    def __init__(self):
        # Initializing logger
        self.logger = Logger(name=__name__)
        self.logger.set_level(Level.DEBUG)
        
        # Initiating the RMRXapp framework from ricxappframe module
        fake_sdl = getenv("USE_FAKE_SDL", False)
        self._rmr_xapp = RMRXapp(self._default_handler,
                                 config_handler=self._handle_config_change,
                                 rmr_port=4560,
                                 post_init=self._post_init,
                                 use_fake_sdl=False) #use_fake_sdl=bool(fake_sdl))

        # Registering handlers for signals
        signal.signal(signal.SIGTERM, self._handle_signal)
        signal.signal(signal.SIGQUIT, self._handle_signal)
        signal.signal(signal.SIGINT, self._handle_signal)

        # Registering callbacks
        self._rmr_xapp.register_callback(handler=self._handle_insert_msg, message_type=Constants.E2_INDICATION_INSERT)

    # Executes after _BaseXapp init but before ending the RMRXapp init
    def _post_init(self, rmr_xapp: RMRXapp):
        """
        Function that runs when xapp initialization is complete
        """
        self.logger.info("post_init called")
        rmr_xapp.logger.set_level(Level.DEBUG)

    def _handle_config_change(self, rmr_xapp, config):
        """
        Function that runs at start and on every configuration file change.
        """
        self.logger.info("handle_config_change:: config: {}".format(config))
        rmr_xapp.config = dict(config)  # No mutex required due to GIL

    def _handle_insert_msg(self, rmr_xapp:RMRXapp, summary, sbuf):
        """
        Function that responds to active xApp RMR message with an ACK
        """
        
        self.logger.info("Received insert message from {} with meID={} and subscription id={}. Replying with a control message.".format(
            summary[rmr.RMR_MS_MSG_SOURCE], summary[rmr.RMR_MS_MEID], summary[rmr.RMR_MS_SUB_ID])
        )

        payload = summary[rmr.RMR_MS_PAYLOAD]
        self.logger.debug("Payload: {}".format(payload))
        try: 
            # asn1obj = e2sm_rc.ASN1Obj()
            asn1obj = e2sm_rc.E2AP_IEs.RICindicationMessage
            decoded = asn1obj.from_aper(payload)
            self.logger.info("Decoded payload: {}".format(decoded()))
        except Exception as e:
            self.logger.error("Error decoding payload: {}".format(e))
        
        # Return the message to the sender with a new message type
        if not rmr_xapp.rmr_rts(sbuf):
            self.logger.error("Control message could not be replied")
        rmr_xapp.rmr_free(sbuf)
    
    def _handle_signal(self, signum: int, frame):
        """
        Function called when a Kubernetes signal is received that stops the xApp execution.
        """
        self.logger.info("Received signal {} to stop the xApp".format(signal.Signals(signum).name))
        self.stop()

    def _default_handler(self, rmr_xapp, summary, sbuf):
        """
        Function that processes messages for which no handler is defined
        """
        self.logger.info("HWXappdefault_handler called for msg type = " + str(summary[rmr.RMR_MS_MSG_TYPE]))
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
        self.appmgr = ApplicationManager(self._rmr_xapp)
        self.rest_mgr = RestManager(self._rmr_xapp)
        self.sub_mgr = SubscriptionManager(self._rmr_xapp)

        self.rest_mgr.start_http_server(8080) # Start the HTTP server to log all received GET and POST messages

        self._rmr_xapp.run(thread=thread, rmr_timeout=5) # Wait 5 second for RMR messages

        # self.logger.info("start:: calling ApplicationManager to register the xApp")
        #self.appmgr.register_xapp()

        # Only gets here if thread=True
        self.logger.info("start:: xApp health check: {}".format(self._rmr_xapp.healthcheck()))
        self.logger.info("start:: calling SubscriptionManager to subscribe to gNBs")
        time.sleep(5) # Wait for the RIC platform to be ready
        self.sub_mgr.subscribe_to_all_gNBs() # Sending subscription requests for gNBs through SubscriptionManager

        

    def stop(self):
        """
        can only be called if thread=True when started
        """
        self.sub_mgr.delete_subscriptions()
        #self.appmgr.deregister_xapp()
        self.rest_mgr.stop_server()
        self._rmr_xapp.stop()
