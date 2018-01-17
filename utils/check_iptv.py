import time
from BLL.agent import ProfileAgent

# Exit statuses recognized by Nagios
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

class Snmp:
    def __init__(self, host):
        self.host = host

    def get_profile_agent_list(self):
        snmp = ProfileAgent()
        data = snmp.get_snmp_profile_agent_list(self.host)
        return data

    def get_human_readable_status(self, status):
        alarm_status = {0:'OK', 1:'WARNING', 2:'CRITICAL', 3:'UNKNOWN'} [status]
        return alarm_status

    def _get_alarm(self, profile_agent_list):
        message = ""
        error_message = ""
        status = OK
        channel_error_num = 0
        count = 0
        for profile_agent in profile_agent_list:
            if profile_agent["monitor"]:
                if profile_agent["status"] != 1:
                    if profile_agent["status"] == 0:
                        error_message += """%s-%s %s NoSource! """%(profile_agent["name"], 
                                                                    profile_agent["type"], 
                                                                    str(profile_agent["ip"]).split(':30120')[0])
                        status = CRITICAL
                        channel_error_num += 1
                    elif profile_agent["status"] == 2:
                        error_message += """%s-%s %s VideoError! """%(profile_agent["name"], 
                                                                    profile_agent["type"], 
                                                                    str(profile_agent["ip"]).split(':30120')[0])
                        status = CRITICAL
                        channel_error_num += 1
                    elif profile_agent["status"] == 3:
                        error_message += """%s-%s %s AudioError! """%(profile_agent["name"], 
                                                                    profile_agent["type"], 
                                                                    str(profile_agent["ip"]).split(':30120')[0])
                        status = CRITICAL
                        channel_error_num += 1
                    else:
                        error_message += """%s-%s %s AudioError! """%(profile_agent["name"], 
                                                                    profile_agent["type"], 
                                                                    str(profile_agent["ip"]).split(':30120')[0])
                        status = CRITICAL
                        channel_error_num += 1
                count += 1
        if status == OK:
            message = """AGENT : %d kenh OK, %d kenh ERROR """%(count - channel_error_num, channel_error_num)
        elif status == CRITICAL:
            message = """AGENT : %d kenh OK, %d kenh ERROR """%(count - channel_error_num, channel_error_num)
        return status, message, error_message

    def check_agent(self):
        start_time = time.time()
        message = ""
        error_message = ""
        status = ""
        data = self.get_profile_agent_list()
        if data["status"] != 200:
            message = data["message"]
            status = WARNING
            error_message = ""
        elif len(data["data"]) == 0:
            status = WARNING
            message = " AGENT : NOT GET INFORMATION "
            error_message = ""
        else:
            profile_agent_list = data["data"]
            status, message, error_message = self._get_alarm(profile_agent_list)
        alarm_status = self.get_human_readable_status(status)
        msg = message + " \n" + error_message + " \n" + "Time to query " + str(round(time.time() - start_time)) + " seconds."
        return alarm_status, msg

    def check_anylazer(self):
        pass



