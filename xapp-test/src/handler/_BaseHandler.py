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

from ricxappframe.xapp_frame import Xapp
from abc import ABC, abstractmethod


class _BaseHandler(ABC):
    """
    Represents base Abstract Handler class
    Here initialize variables which will be common to all xapp

    Parameters:
        xapp: Reference to original xappframe object
        msgtype: Integer specifying messagetype
    """

    def __init__(self, xapp: Xapp, msgtype):
        self._xapp = xapp
        self.logger = self._xapp.logger
        self.msgtype = msgtype
        #self._xapp.register_callback(self.request_handler, msgtype)

    @abstractmethod
    def request_handler(self, xapp, summary, sbuf):
        pass
