import json
import logging
import requests
from scc_request import ApiRequest
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
                queueBegin = json_data['queueBegin']
            else:
                queueBegin = self.now
            if "queueQty" in json_data:
                queueQty = json_data['queueQty']
            else:
                queueQty = 0
            if "isHost" in json_data:
                isHost = json_data['isHost']
            else:
                isHost = False
            if "queueServiceName" in json_data:
                queueServiceName = json_data['queueServiceName']
            else:
                queueServiceName = None
            if "settingTime" in json_data:
                settingTime = json_data['settingTime']
            else:
                settingTime = self.now
            if "createdIncident" in json_data:
                createdIncident = json_data['createdIncident']
            else:
                createdIncident = False
            if "queueAlertID" in json_data:
                queueAlertID = json_data['queueAlertID']
            else:
                queueAlertID = None
            if "queueStatus" in json_data:
                queueStatus = json_data['queueStatus']
            else:
                queueStatus = 'normal'
            if "queueHost" in json_data:
                queueHost = json_data['queueHost']
            else:
                queueHost = None
            if "incidentTicketID" in json_data:
                incidentTicketID = json_data['incidentTicketID']
            else:
                incidentTicketID = None
            if "msg" in json_data:
                msg = json_data['msg']
            else:
                msg = None
            if "AlertStatus" in json_data:
                AlertStatus = json_data['AlertStatus']
            else:
                AlertStatus = None

            data = [{
                        "queueBegin" : queueBegin,
                        "queueQty" : queueQty,
                        "isHost" : isHost,
                        "queueServiceName" : queueServiceName,
                        "settingTime" : settingTime,
                        "createdIncident" : createdIncident,
                        "queueAlertID" : queueAlertID,
                        "queueStatus" : queueStatus,
                        "queueHost" : queueHost,
                        "incidentTicketID" : incidentTicketID,
                        "msg" : msg,
                        "AlertStatus" : AlertStatus
                    }]
            data = json.dumps(data)
            rsp = self.scc_api.post(data)
            self.logger.debug("status: %d, message: %s"%(0, str(rsp)))
            return rsp
        except Exception as e:
            self.logger.error("status: %d, message: %s"%(1, str(e)))
            return None

