# encoding=utf8
import json
import logging
import requests
from scc_request_v2 import ApiRequest
from utils.DateTime import DateTime

class Scc:
    def __init__(self):
        self.logger = logging.getLogger("scc")
        date_time = DateTime()
        self.now = date_time.get_now_as_isofortmat()
        self.scc_api = ApiRequest() 

    def post(self, json_data):
        try:
            if "queueBegin" in json_data:
                EventDateTime = json_data['queueBegin']
            else:
                EventDateTime = self.now
            if "queueServiceName" in json_data:
                ServiceName = json_data['queueServiceName']
            else:
                ServiceName = None
            if "queueHost" in json_data:
                HostName = json_data['queueHost']
            else:
                HostName = None
            if "msg" in json_data:
                msg = json_data['msg']
            else:
                msg = None
            if "AlertStatus" in json_data:
                ServiceState = json_data['AlertStatus']
            else:
                ServiceState = None
            if "agentId" in json_data:
                agentId = json_data['agentId']
            else:
                agentId = 0

            data = {   "AlertPlan": "Hệ thống IPTV".decode("utf-8"),
                        "HostName": HostName,
                        "EventID": agentId,
                        "ObjectID": agentId,
                        "Output": msg,
                        "ServiceName": ServiceName,
                        "HostState": "None",
                        "ServiceState": ServiceState,
                        "EventDateTime": EventDateTime
                    }
            data = json.dumps(data)
            rsp = self.scc_api.post(data)
            self.logger.debug("status: %d, message: %s"%(0, str(rsp)))
            return rsp
        except Exception as e:
            self.logger.error("status: %d, message: %s"%(1, str(e)))
            return None

