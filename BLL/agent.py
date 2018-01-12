from DAL.agent import ProfileAgent as ProfileAgentDAL

class ProfileAgent:
    def __init__(self):
        self.pa = ProfileAgentDAL()

    def get_monitor_profile_agent_list(self, ip):
        return self.pa.get_monitor_profile_agent_list(ip)

    def get_snmp_profile_agent_list(self, ip):
        return self.pa.get_snmp_profile_agent_list(ip)

    def get_first_check_anylazer_profile_agent_list(self):
        return self.pa.get_first_check_anylazer_profile_agent_list()

    def get_last_check_analyzer_profile_agent_list(self):
        return self.pa.get_last_check_analyzer_profile_agent_list()

