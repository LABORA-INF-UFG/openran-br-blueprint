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
        nb_id_json = {
            'inventory_name': nb_id.inventory_name.decode('utf-8') if isinstance(nb_id.inventory_name, bytes) else nb_id.inventory_name,
            'global_nb_id': {
                'plmn_id': nb_id.global_nb_id.plmn_id.decode('utf-8') if isinstance(nb_id.global_nb_id.plmn_id, bytes) else nb_id.global_nb_id.plmn_id,
                'nb_id': nb_id.global_nb_id.nb_id.decode('utf-8') if isinstance(nb_id.global_nb_id.nb_id, bytes) else nb_id.global_nb_id.nb_id,
            },
            'connection_status': nb_id.connection_status,
        }
        self.logger.info("SubscriptionManager.nb_to_dict:: Processed request: {}".format(nb_id_json))
        return nb_id_json

    def nb_list_to_dict(self, nb_id_list):
        nb_id_dict_list = [self.nb_to_dict(nb_id) for nb_id in nb_id_list]
        self.logger.info("SubscriptionManager.nb_list_to_dict:: Processed request: {}".format(nb_id_dict_list))
        return nb_id_dict_list

    def get_gnb_list(self):
        gnblist = self.nb_list_to_dict(self._rmr_xapp.get_list_gnb_ids())
        self.logger.info("SubscriptionManager.getGnbList:: Processed request: {}".format(gnblist))
        return gnblist

    def get_enb_list(self):
        enblist = self.nb_list_to_dict(self._rmr_xapp.get_list_enb_ids())
        self.logger.info("SubscriptionManager.sdlGetGnbList:: Handler processed request: {}".format(self.nb_list_to_dict(enblist)))
        return enblist

    def send_subscription_request(self, xnb_inventory_name, subscription_transaction_id):
        self.logger.info("SubscriptionManager.send_subscription_request:: Sending subscription request to {}".format(xnb_inventory_name))
        # subscription_request = {"xnb_id": self.nb_to_dict(xnb_id), "action_type": Constants.ACTION_TYPE}
        subscription_request = {
            "SubscriptionId":"",
            "ClientEndpoint": {
                "Host":"service-ricxapp-bouncerxapp-http.ricxapp",
                "HTTPPort":8080,
                "RMRPort":4560
            },
            "Meid":xnb_inventory_name, # nobe B inventory_name
            "RANFunctionID":0, # Check in the E2 SIM
            # "E2SubscriptionDirectives":{ # Optional, using default sub mgr values
            #     "E2TimeoutTimerValue":2,
            #     "E2RetryCount":2,
            #     "RMRRoutingNeeded":True
            # },
            "SubscriptionDetails":[ # Can make multiple subscriptions
                {
                    "XappEventInstanceId":subscription_transaction_id, # "Transaction id"
                    "EventTriggers":[0],
                    "ActionToBeSetupList":[
                        {
                            "ActionID": 1,
                            "ActionType": "report",
                            "ActionDefinition": [0],
                            "SubsequentAction":{
                                "SubsequentActionType":"continue",
                                "TimeToWait":"zero"
                            }
                        }
                    ]
                }
            ]
        }
        
        try:
            json_object = json.dumps(subscription_request,indent=4)
        except TypeError:
            self.logger.error("SubscriptionManager.send_subscription_request:: Unable to serialize the object")
        # url = Constants.SUBSCRIPTION_PATH.format(Constants.PLT_NAMESPACE,
        #                                          Constants.SUBSCRIPTION_SERVICE,
        #                                          Constants.SUBSCRIPTION_PORT)
        # url = "http://service-ricplt-submgr-http:3800" # Original
        url = "http://service-ricplt-submgr-http.ricplt.svc.cluster.local:8088/ric/v1/subscriptions" # RIC-O
        try:
            self.logger.info("SubscriptionManager.send_subscription_request:: Sending Node B subscription request to {}: {}".format(url, subscription_request))
            response = requests.post(url, json=subscription_request) #data=subscription_request) #json=json_object)
            if response.status_code == 201:
                data = response.json()
                self.logger.info("SubscriptionManager.send_subscription_request:: Received OK response from Node B subscription request with data: {}".format(data))
                sub_id = data["SubscriptionId"]
                sub_instancies = data["SubscriptionInstances"]
            else:
                self.logger.info("SubscriptionManager.send_subscription_request:: Received response from Node B subscription request with code: {}".format(response.status_code))
            response.raise_for_status()
        except requests.exceptions.HTTPError as err_h:
            self.logger.error("SubscriptionManager.send_subscription_request:: An Http Error occurred:" + repr(err_h))
        except requests.exceptions.ConnectionError as err_c:
            self.logger.error("SubscriptionManager.send_subscription_request:: An Error Connecting to the API occurred:" + repr(err_c))
        except requests.exceptions.Timeout as err_t:
            self.logger.error("SubscriptionManager.send_subscription_request:: A Timeout Error occurred:" + repr(err_t))
        except requests.exceptions.RequestException as err:
            self.logger.error("SubscriptionManager.send_subscription_request:: An Unknown Error occurred" + repr(err))







