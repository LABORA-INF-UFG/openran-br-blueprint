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

import json
from ricxappframe.xapp_frame import Xapp
from ..utils.constants import Constants
from ._BaseHandler import _BaseHandler
# from ..manager import SdlAlarmManager


class HealthCheckHandler(_BaseHandler):

    def __init__(self, xapp: Xapp, msgtype):
        super().__init__(xapp, msgtype)
        # self.sdl_alarm_mgr = SdlAlarmManager()

    def request_handler(self, xapp, summary, sbuf):
        ok = self._xapp.healthcheck()
        # self.sdl_alarm_mgr.checkSdl()
        if ok:
            payload = b"OK\n"
        else:
            payload = b"ERROR [RMR or SDL is unhealthy]\n"
        self._xapp.rmr_rts(sbuf, new_payload=payload, new_mtype=Constants.RIC_HEALTH_CHECK_RESP)
        self._xapp.rmr_free(sbuf)
