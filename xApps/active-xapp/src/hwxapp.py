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


from .utils.constants import Constants
from .manager import *

from .handler import *
from mdclogpy import Logger
from mdclogpy import Level

class HWXapp:

    def __init__(self):
        fake_sdl = getenv("USE_FAKE_SDL", False)
        self._xapp = Xapp(self._loop,
                                 #config_handler=self._handle_config_change,
                                 rmr_port=4560,
                                 #post_init=self._post_init,
                                 use_fake_sdl=bool(fake_sdl))

    def _post_init(self, xapp: Xapp):
        """
        Function that runs when xapp initialization is complete
        """
        
        xapp.logger.set_level(Level.DEBUG)
        # xapp.logger.info("Level INFO")
        # xapp.logger.error("Level ERROR")
        # xapp.logger.warning("Level WARNING")
        # xapp.logger.debug("Level DEBUG")

        xapp.logger.info("HWXapp.post_init :: post_init called")

        # Shared Data Layer (SDL)
        sdl_mgr = SdlManager(xapp)
        sdl_mgr.sdlGetGnbList()

        # SDL Alarm Manager (doesn't work because environmental variables are missing)
        # Missing env vars: ALARM_MGR_SERVICE_NAME, ALARM_MGR_SERVICE_PORT
        #self.sdl_alarm_mgr = SdlAlarmManager(xapp)
        #self.sdl_alarm_mgr.checkSdl()

        # A1 Manager
        # Non-RT RIC is not running
        #a1_mgr = A1PolicyManager(xapp)
        #a1_mgr.startup()

        # Subscription Manager
        sub_mgr = SubscriptionManager(xapp)

        enb_list = sub_mgr.get_enb_list() # Getting eNodeBs
        xapp.logger.info("Number of eNBs: {}".format(len(enb_list)))
        for enb in enb_list:
            sub_mgr.send_subscription_request(enb)

        gnb_list = sub_mgr.get_gnb_list() # Getting gNodeBs
        xapp.logger.info("Number of gNBs: {}".format(len(gnb_list)))
        for gnb in gnb_list:
            sub_mgr.send_subscription_request(gnb)

        # Metric Manager (I don't remember it on the RIC architecture)
        metric_mgr = MetricManager(xapp)
        metric_mgr.send_metric()

    def _handle_config_change(self, xapp, config):
        """
        Function that runs at start and on every configuration file change.
        """
        xapp.logger.info("HWXapp.handle_config_change:: config: {}".format(config))
        xapp.config = config  # No mutex required due to GIL
        
    def _default_handler(self, xapp, summary, sbuf):
        """
        Function that processes messages for which no handler is defined
        """
        xapp.logger.info("HWXapp.default_handler called for msg type = " +
                                   str(summary[rmr.RMR_MS_MSG_TYPE]))
        xapp.rmr_free(sbuf)

    def createHandlers(self):
        """
        Function that creates all the handlers for RMR Messages
        """
        HealthCheckHandler(self._xapp, Constants.RIC_HEALTH_CHECK_REQ)
        A1PolicyHandler(self._xapp, Constants.A1_POLICY_REQ)
        SubscriptionHandler(self._xapp,Constants.SUBSCRIPTION_REQ)

    # TODO: change "while True" to a flag indicating that the xApp is not being terminated
    def _loop (self, xapp):
        """
        Function that runs in loop from the xApp start until its end
        """
        xapp.logger.info("Running loop")
        i = 0
        while True:
            self._xapp.logger.info("Sending message to reactive xApp")
            xapp.rmr_send("Request {}".format(i).encode(), 30000)
            i+=1
        xapp.logger.info("Ended loop")

    def start(self):
        """
        This is a convenience function that allows this xapp to run in Docker
        for "real" (no thread, real SDL), but also easily modified for unit testing
        (e.g., use_fake_sdl). The defaults for this function are for the Dockerized xapp.
        """
        self._xapp.logger.set_level(Level.DEBUG)
        self.createHandlers()
        self._xapp.run()

    def stop(self):
        """
        can only be called if thread=True when started
        TODO: could we register a signal handler for Docker SIGTERM that calls this?
        """
        self._xapp.stop()
