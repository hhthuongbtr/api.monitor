import time
import json
import logging
from BLL.agent import ProfileAgent
from setting.settings import SYSTEM
from DateTime import DateTime


# Exit statuses recognized by Nagios
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

class Snmp:
    def __init__(self, host):
        self.host = host
        self.logger = logging.getLogger("utils")

    def get_profile_agent_list(self):
        snmp = ProfileAgent()
        data = snmp.get_profile_agent_snmp_list(self.host)
        return data

    def get_human_readable_status(self, status):
        alarm_status = {0: "OK", 1: "WARNING", 2: "CRITICAL", 3: "UNKNOWN"} [status]
        return alarm_status

    def _get_alarm(self, profile_agent_list):
        message = ""
        error_message_list = []
        status = OK
        channel_error_num = 0
        count = 0
        for profile_agent in profile_agent_list:
            if profile_agent["monitor"]:
                if profile_agent["status"] == 1 and profile_agent["video_status"] != 1:
                    profile_status = 2
                else:
                    profile_status = profile_agent["status"]
                if profile_status != 1:
                    status = CRITICAL
                    channel_error_num += 1
                    if profile_status == 0:
                        error = "NoSource!"
                    elif profile_status == 2:
                        error = "VideoError!"
                    elif profile_status == 3:
                        error = "AudioError"
                    else:
                        error = "Unknow"
                    error_message = {
                                        "Channel": profile_agent["name"], 
                                        "Type": profile_agent["type"],
                                        "Ip": str(profile_agent["ip"]).split(":30120")[0], 
                                        "AlarmStatus": error
                    }

                    error_message_list.append(error_message)
                count += 1
        self.logger.info("alarm - %s - %s"%(self.host, str(error_message_list)))
        if status == OK:
            message = """AGENT : %d kenh OK, %d kenh ERROR """%(count - channel_error_num, channel_error_num)
        elif status == CRITICAL:
            message = """AGENT : %d kenh OK, %d kenh ERROR """%(count - channel_error_num, channel_error_num)
        return status, message, error_message_list

    def _get_alarm_video(self, profile_agent_list):
        message = ""
        error_message_list = []
        status = OK
        channel_error_num = 0
        count = 0
        for profile_agent in profile_agent_list:
            if profile_agent["monitor"]:
                if profile_agent['status'] == 1 and profile_agent['video_status'] != 1:
                    profile_agent_status = 2
                else:
                    profile_agent_status = profile_agent['status']
                if profile_agent_status != 1:
                    status = CRITICAL
                    channel_error_num += 1
                    if profile_agent_status == 0:
                        error = "NoSource!"
                    elif profile_agent_status == 2:
                        error = "VideoError!"
                    elif profile_agent_status == 3:
                        error = "AudioError"
                    else:
                        error = "Unknow"
                    error_message = {
                                        "Channel": profile_agent["name"], 
                                        "Type": profile_agent["type"],
                                        "Ip": str(profile_agent["ip"]).split(':30120')[0], 
                                        "AlarmStatus": error
                    }

                    error_message_list.append(error_message)
                count += 1
        self.logger.info("alarm-video - %s - %s"%(self.host, str(error_message_list)))
        if status == OK:
            message = """AGENT : %d kenh OK, %d kenh ERROR """%(count - channel_error_num, channel_error_num)
        elif status == CRITICAL:
            message = """AGENT : %d kenh OK, %d kenh ERROR """%(count - channel_error_num, channel_error_num)
        return status, message, error_message_list

    def check_agent(self):
        start_time = time.time()
        message = ""
        error_message = ""
        status = ""
        error_message_list = []
        data = self.get_profile_agent_list()
        if data["status"] != 200:
            message = data["message"]
            status = WARNING
            error_message = ""
            self.logger.warning("status: %d message: %s"%(status, "Empty"))
        elif len(data["data"]) == 0:
            status = WARNING
            message = " AGENT : NOT GET INFORMATION "
            error_message = ""
            self.logger.info("status: %d message: %s"%(status, "Empty"))
        else:
            profile_agent_list = data["data"]
            date_time = DateTime()
            now = date_time.get_now()
            HH = date_time.get_hour(now)
            if HH > SYSTEM["broadcast_time"]["FROM"] and HH < SYSTEM["broadcast_time"]["TO"]:
                status, message, error_message_list = self._get_alarm_video(profile_agent_list)
            else:
                status, message, error_message_list = self._get_alarm(profile_agent_list)
        alarm_status = self.get_human_readable_status(status)
        msg = {
                    "Message": message, 
                    "Data": json.dumps(error_message_list), 
                    "ProcessingTime": "Time to query " + str(round(time.time() - start_time)) + " seconds."
        }
        return alarm_status, msg

    def check_anylazer(self):
        pass