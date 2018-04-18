from DAL import ProfileAgent as ProfileAgentDAL

class ProfileAgent:
    def __init__(self):
        self.pa = ProfileAgentDAL()

    def get_profile_agent_monitor_list(self, ip):
        return self.pa.get_profile_agent_monitor_list(ip)

    def get_profile_agent_snmp_list(self, ip):
        return self.pa.get_profile_agent_snmp_list(ip)

    def get_profile_agent_check_video_list(self, ip):
        return self.pa.get_profile_agent_check_video_list(ip)

    def get_profile_agent_first_check_anylazer_list(self):
        return self.pa.get_profile_agent_first_check_anylazer_list()

    def get_profile_agent_last_check_analyzer_list(self):
        return self.pa.get_profile_agent_last_check_analyzer_list()

