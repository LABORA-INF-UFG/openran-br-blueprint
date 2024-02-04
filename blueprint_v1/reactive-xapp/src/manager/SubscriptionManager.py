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
from ..utils.constants import Constants
from ._BaseManager import _BaseManager
from ricxappframe.entities.rnib.nb_identity_pb2 import NbIdentity
from ricxappframe.entities.rnib.nodeb_info_pb2 import Node

class SubscriptionManager(_BaseManager):

    __namespace = "e2Manager"

    def __init__(self, rmr_xapp: RMRXapp):
        super().__init__(rmr_xapp)

    def nb_to_dict(self, nb_id):
        return {
            'inventory_name': nb_id.inventory_name.decode('utf-8') if isinstance(nb_id.inventory_name, bytes) else nb_id.inventory_name,
            'global_nb_id': {
                'plmn_id': nb_id.global_nb_id.plmn_id.decode('utf-8') if isinstance(nb_id.global_nb_id.plmn_id, bytes) else nb_id.global_nb_id.plmn_id,
                'nb_id': nb_id.global_nb_id.nb_id.decode('utf-8') if isinstance(nb_id.global_nb_id.nb_id, bytes) else nb_id.global_nb_id.nb_id,
            },
            'connection_status': nb_id.connection_status,
        }

    def nb_list_to_dict(self, nb_id_list):
        return [self.nb_to_dict(nb_id) for nb_id in nb_id_list]

    def get_gnb_list(self):
        gnblist = self._rmr_xapp.get_list_gnb_ids()
        self.logger.info("SubscriptionManager.getGnbList:: Processed request: {}".format(self.nb_list_to_dict(gnblist)))
        return gnblist

    def get_enb_list(self):
        enblist = self._rmr_xapp.get_list_enb_ids()
        self.logger.info("SubscriptionManager.sdlGetGnbList:: Handler processed request: {}".format(self.nb_list_to_dict(enblist)))
        return enblist

    def send_subscription_request(self,xnb_id):
        subscription_request = {"xnb_id": self.nb_to_dict(xnb_id), "action_type": Constants.ACTION_TYPE}
        try:
            json_object = json.dumps(subscription_request,indent=4)
        except TypeError:
            self.logger.error("SubscriptionManager.send_subscription_request:: Unable to serialize the object")
        url = Constants.SUBSCRIPTION_PATH.format(Constants.PLT_NAMESPACE,
                                                 Constants.SUBSCRIPTION_SERVICE,
                                                 Constants.SUBSCRIPTION_PORT)
        try:
            self.logger.info("SubscriptionManager.send_subscription_request:: Sending Node B subscription request: {}".format(subscription_request))
            response = requests.post(url , json=json_object)
            self.logger.info("SubscriptionManager.send_subscription_request:: Received response from Node B subscription request: {}".format(response))
            response.raise_for_status()
        except requests.exceptions.HTTPError as err_h:
            self.logger.error("SubscriptionManager.send_subscription_request:: An Http Error occurred:" + repr(err_h))
        except requests.exceptions.ConnectionError as err_c:
            self.logger.error("SubscriptionManager.send_subscription_request:: An Error Connecting to the API occurred:" + repr(err_c))
        except requests.exceptions.Timeout as err_t:
            self.logger.error("SubscriptionManager.send_subscription_request:: A Timeout Error occurred:" + repr(err_t))
        except requests.exceptions.RequestException as err:
            self.logger.error("SubscriptionManager.send_subscription_request:: An Unknown Error occurred" + repr(err))







