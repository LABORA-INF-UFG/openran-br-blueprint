# ==================================================================================
#
#       Copyright (c) 2021 Samsung Electronics Co., Ltd. All Rights Reserved.
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
"""

"""

import requests
from ricxappframe.xapp_frame import RMRXapp
import json
import os
from ..utils.constants import Constants
from ._BaseManager import _BaseManager

class ApplicationManager(_BaseManager):

    def __init__(self, rmr_xapp: RMRXapp):
        super().__init__(rmr_xapp)
        # self._config_data = None
        # if self._config_path and os.path.isfile(self._config_path):
        #     with open(self._config_path) as json_file:
        #         self._config_data = json.load(json_file)
        # if self._config_data is None or not isinstance(self._config_data, dict):
        #     self.logger.error("ApplicationManager.__init__:: Failed to load config data from file: {}".format(self._config_path))
        # self._config_data = self._rmr_xapp._config_data
        # if self._config_data is None:
        #     self.logger.error("ApplicationManager.__init__:: Failed to load config data from xApp")
        # else:
        #     self.logger.info("ApplicationManager.__init__:: Config data loaded succesfully: {}".format(self._config_data))

    def register_xapp(self):
        registration_request = {
            "appName": os.environ.get("HOSTNAME"),
            "appVersion": self._rmr_xapp.config.get("version"),
            "configPath": "",
            "appInstanceName": self._rmr_xapp.config.get("name"),
            "httpEndpoint": "service-ricxapp-bouncerxapp-http.ricxapp:8080",
            "rmrEndpoint": "service-ricxapp-bouncerxapp-rmr.ricxapp:4560",
            "config": self._rmr_xapp.config #json.dumps(self._rmr_xapp.config)
		}
        url = "http://service-ricplt-appmgr-http.ricplt.svc.cluster.local:8080/ric/v1/register"
        try:
            self.logger.info("ApplicationManager.register_xapp:: Sending xApp registration request to {}: {}".format(url, registration_request))
            response = requests.post(url, json=registration_request)
            self.logger.info("ApplicationManager.register_xapp:: Received response from AppMgr registration request with code: {}".format(response.status_code))
            data = response.json()
            if data is None:
                self.logger.error("ApplicationManager.register_xapp:: Received response from AppMgr registration request with code: {} and no data".format(response.status_code))
            else:
                self.logger.info("ApplicationManager.register_xapp:: Received response from AppMgr registration request with code: {} and data: {}".format(response.status_code, data))
            response.raise_for_status()
        except requests.exceptions.HTTPError as err_h:
            self.logger.error("ApplicationManager.register_xapp:: An Http Error occurred:" + repr(err_h))
        except requests.exceptions.ConnectionError as err_c:
            self.logger.error("ApplicationManager.register_xapp:: An Error Connecting to the API occurred:" + repr(err_c))
        except requests.exceptions.Timeout as err_t:
            self.logger.error("ApplicationManager.register_xapp:: A Timeout Error occurred:" + repr(err_t))
        except requests.exceptions.RequestException as err:
            self.logger.error("ApplicationManager.register_xapp:: An Unknown Error occurred" + repr(err))
    
    def deregister_xapp(self):
        deregistration_request = {
            "appName": os.environ.get("HOSTNAME"),
            "appInstanceName": self._rmr_xapp.config.get("name"),
		}
        url = "http://service-ricplt-appmgr-http.ricplt.svc.cluster.local:8080/ric/v1/deregister"
        try:
            self.logger.info("ApplicationManager.register_xapp:: Sending xApp deregistration request to {}: {}".format(url, deregistration_request))
            response = requests.post(url, json=deregistration_request)
            self.logger.info("ApplicationManager.register_xapp:: Received response from AppMgr deregistration request with code: {}".format(response.status_code))
            data = response.json()
            if data is None:
                self.logger.error("ApplicationManager.register_xapp:: Received response from AppMgr deregistration request with code: {} and no data".format(response.status_code))
            else:
                self.logger.info("ApplicationManager.register_xapp:: Received response from AppMgr deregistration request with code: {} and data: {}".format(response.status_code, data))
            response.raise_for_status()
        except requests.exceptions.HTTPError as err_h:
            self.logger.error("ApplicationManager.register_xapp:: An Http Error occurred:" + repr(err_h))
        except requests.exceptions.ConnectionError as err_c:
            self.logger.error("ApplicationManager.register_xapp:: An Error Connecting to the API occurred:" + repr(err_c))
        except requests.exceptions.Timeout as err_t:
            self.logger.error("ApplicationManager.register_xapp:: A Timeout Error occurred:" + repr(err_t))
        except requests.exceptions.RequestException as err:
            self.logger.error("ApplicationManager.register_xapp:: An Unknown Error occurred" + repr(err))