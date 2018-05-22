import json
import logging
from MySQL_Database import Database

class ProfileAgent:
    def __init__(self):
        self.db = Database()
        self.logger = logging.getLogger("probe")
    """
    Monitor list
    """
    def convert_profile_agent_monitor_list_to_array(self, data_table):
        args = []
        for profile_agent in data_table:
            try:
                args.append({ 
                                'id'            : profile_agent[0] if profile_agent[0] else None,
                                'ip'            : profile_agent[1] if profile_agent[1] else "",
                                'protocol'      : profile_agent[2] if profile_agent[2] else 'udp',
                                'status'        : profile_agent[3] if profile_agent[3] else 0,
                                'agent'         : profile_agent[4] if profile_agent[4] else "",
                                'thread'        : profile_agent[5] if profile_agent[5] else 10,
                                'name'          : profile_agent[6] if profile_agent[6] else "",
                                'type'          : profile_agent[7] if profile_agent[7] else None
                            })
            except Exception as e:
                self.logger.error("error: %d, message: %s"%(1, str(e)))
        return args

    def get_profile_agent_monitor_list(self, ip):
        http_status_code = 500
        message = "Unknow"
        data = None
        sql = """select pa.id, p.ip, p.protocol, pa.status, a.name as agent, a.thread, c.name, p.type
            from profile as p, agent as a, profile_agent as pa,channel as c 
            where a.ip='%s' and a.active=1 and pa.monitor=1 and p.channel_id=c.id and pa.profile_id=p.id and pa.agent_id=a.id"""%(ip)
        status, message, data_table = self.db.execute_query(sql)
        if status == 1:
            http_status_code = 500
            message = message
            data = None
            self.logger.error("ststus: %d, message: %s"%(http_status_code, message))
        if status == 0:
            http_status_code = 200
            message = message
            data = self.convert_profile_agent_monitor_list_to_array(data_table)
            self.logger.debug("ststus: %s, message: total %d"%(http_status_code, len(data)))
        json_response = {"status": http_status_code, "message": message, "data": data}
        json_response = json.dumps(json_response)
        json_response = json.loads(json_response)
        return json_response

    def get_profile_agent_monitor_list_by_source_ip_multicast(self, ip, source):
        http_status_code = 500
        message = "Unknow"
        data = None
        sql = """select pa.id, p.ip, p.protocol, pa.status, a.name as agent, a.thread, c.name, p.type
            from profile as p, agent as a, profile_agent as pa,channel as c 
            where p.ip LIKE '%s:%%' and a.ip='%s' and a.active=1 and pa.monitor=1 and p.channel_id=c.id and pa.profile_id=p.id and pa.agent_id=a.id"""%(source,ip)
        status, message, data_table = self.db.execute_query(sql)
        if status == 1:
            http_status_code = 500
            message = message
            data = None
            self.logger.error("ststus: %d, message: %s"%(http_status_code, message))
        if status == 0:
            http_status_code = 200
            message = message
            data = self.convert_profile_agent_monitor_list_to_array(data_table)
            self.logger.debug("ststus: %s, message: total %d"%(http_status_code, len(data)))
        json_response = {"status": http_status_code, "message": message, "data": data}
        json_response = json.dumps(json_response)
        json_response = json.loads(json_response)
        return json_response

    """
    Snmp list
    """
    def convert_profile_agent_snmp_list_to_array(self, data_table):
        args = []
        for profile_agent in data_table:
            try:
                args.append({ 
                                'id'                     : profile_agent[0] if profile_agent[0] else None,
                                'name'                   : profile_agent[1] if profile_agent[1] else "",
                                'ip'                     : profile_agent[2] if profile_agent[2] else "",
                                'type'                   : profile_agent[3] if profile_agent[3] else "",
                                'monitor'                : profile_agent[4] if profile_agent[4] else 0,
                                'status'                 : profile_agent[5] if profile_agent[5] else 0,
                                'analyzer'               : profile_agent[6] if profile_agent[6] else 0,
                                'analyzer_status'        : profile_agent[7] if profile_agent[7] else 0,
                                "video_status"           : profile_agent[8] if profile_agent[8] else 0
                            })
            except Exception as e:
                self.logger.error("error: %d, message: %s"%(1, str(e)))
        return args

    def get_profile_agent_snmp_list(self, ip):
        sql = """select pa.id, c.name, p.ip, p.type, pa.monitor, pa.status, pa.analyzer, pa.analyzer_status, pa.video 
            from profile as p, agent as a, profile_agent as pa,channel as c 
            where a.ip='%s' and (pa.monitor=1 or pa.analyzer=1) and a.active=1 and p.channel_id=c.id and pa.profile_id=p.id and pa.agent_id=a.id order by c.name"""%(ip)
        status, message, data_table = self.db.execute_query(sql)
        if status == 1:
            http_status_code = 500
            message = message
            data = None
            self.logger.error("ststus: %d, message: %s"%(http_status_code, message))
        if status == 0:
            http_status_code = 200
            message = message
            data = self.convert_profile_agent_snmp_list_to_array(data_table)
            self.logger.debug("ststus: %s, message: total %d"%(http_status_code, len(data)))
        json_response = {"status": http_status_code, "message": message, "data": data}
        json_response = json.dumps(json_response)
        json_response = json.loads(json_response)
        return json_response

    """
    check video
    """
    def convert_profile_agent_check_video_list_to_array(self, data_table):
        args = []
        for profile_agent in data_table:
            try:
                args.append({ 
                                "id"                : profile_agent[0] if profile_agent[0] else None,
                                "ip"                : profile_agent[1] if profile_agent[1] else "",
                                "protocol"          : profile_agent[2] if profile_agent[2] else "udp",
                                "status"            : profile_agent[3] if profile_agent[3] else 0,
                                "thread"            : profile_agent[4] if profile_agent[4] else 10,
                                "name"              : profile_agent[5] if profile_agent[5] else "Unknow",
                                "agent"             : profile_agent[6] if profile_agent[6] else "Unknow",
                                "type"              : profile_agent[7] if profile_agent[7] else "",
                                "video_status"      : profile_agent[8] if profile_agent[8] else 0

                            })
            except Exception as e:
                self.logger.error("error: %d, message: %s"%(1, str(e)))
        return args

    def get_profile_agent_check_video_list(self, ip):
        sql = """select pa.id, p.ip, p.protocol, pa.status, a.thread, c.name, a.name as agent_name, p.type, pa.video 
            from profile as p, agent as a, profile_agent as pa, channel as c 
            where a.ip = '%s' and a.active = 1 and pa.monitor = 1 and (pa.status = 1 or pa.video !=1) and pa.profile_id = p.id and pa.agent_id = a.id and p.channel_id = c.id"""%(ip)
        status, message, data_table = self.db.execute_query(sql)
        if status == 1:
            http_status_code = 500
            message = message
            data = None
            self.logger.error("ststus: %d, message: %s"%(http_status_code, message))
        if status == 0:
            http_status_code = 200
            message = message
            data = self.convert_profile_agent_check_video_list_to_array(data_table)
            self.logger.debug("ststus: %s, message: total %d"%(http_status_code, len(data)))
        json_response = {"status": http_status_code, "message": message, "data": data}
        json_response = json.dumps(json_response)
        json_response = json.loads(json_response)
        return json_response

    """
    Anylazer first check list
    """
    def convert_profile_agent_first_check_anylazer_list_to_array(self, data_table):
        args = []
        for profile_agent in data_table:
            try:
                args.append({
                                'id'            : profile_agent[0] if profile_agent[0] else None,
                                'ip'            : profile_agent[1] if profile_agent[1] else "",
                                'agent_ip'      : profile_agent[2] if profile_agent[2] else "",
                                'dropframe'     : profile_agent[3] if profile_agent[3] else 0,
                                'discontinuity' : profile_agent[4] if profile_agent[4] else 0
                            })
            except Exception as e:
                self.logger.error("error: %d, message: %s"%(1, str(e)))

        return args

    def get_profile_agent_first_check_anylazer_list(self):
        sql = """select pa.id,p.ip,a.ip,dropframe,discontinuity 
            from profile_agent as pa, profile as p, agent as a 
            where pa.analyzer=1 and a.active=1 and pa.profile_id=p.id and pa.agent_id=a.id"""
        status, message, data_table = self.db.execute_query(sql)
        if status == 1:
            http_status_code = 500
            message = message
            data = None
            self.logger.error("ststus: %d, message: %s"%(http_status_code, message))
        if status == 0:
            http_status_code = 200
            message = message
            data = self.convert_profile_agent_first_check_anylazer_list_to_array(data_table)
            self.logger.debug("ststus: %s, message: total %d"%(http_status_code, len(data)))
        json_response = {"status": http_status_code, "message": message, "data": data}
        json_response = json.dumps(json_response)
        json_response = json.loads(json_response)
        return json_response

    """
    Anylazer last check list
    """
    def convert_profile_agent_last_check_analyzer_list_to_array(self, data_table):
        args = []
        for profile_agent in data_table:
            try:
                args.append({
                            'id'                     : profile_agent[0] if profile_agent[0] else None,
                            'ip'                     : profile_agent[1] if profile_agent[1] else "",
                            'agent_ip'               : profile_agent[2] if profile_agent[2] else "",
                            'analyzer_status'        : profile_agent[3] if profile_agent[3] else 0,
                            'dropframe'              : profile_agent[4] if profile_agent[4] else 0,
                            'dropframe_threshold'    : profile_agent[5] if profile_agent[5] else 0,
                            'discontinuity'          : profile_agent[6] if profile_agent[6] else 0,
                            'discontinuity_threshold': profile_agent[7] if profile_agent[7] else 0,
                        })
            except Exception as e:
                self.logger.error("error: %d, message: %s"%(1, str(e)))
        return args

    def get_profile_agent_last_check_analyzer_list(self):
        sql = """select pa.id, p.ip, a.ip, pa.analyzer_status, pa.dropframe, pa.dropframe_threshold, pa.discontinuity, pa.discontinuity_threshold 
            from profile_agent as pa, profile as p, agent as a 
            where (pa.dropframe > 0 or pa.discontinuity > 0 or analyzer_status !=1) and a.active=1 and pa.analyzer=1 and pa.profile_id=p.id and pa.agent_id=a.id"""
        status, message, data_table = self.db.execute_query(sql)
        if status == 1:
            http_status_code = 500
            message = message
            data = None
            self.logger.error("ststus: %d, message: %s"%(http_status_code, message))
        if status == 0:
            http_status_code = 200
            message = message
            data = self.convert_profile_agent_last_check_analyzer_list_to_array(data_table)
            self.logger.debug("ststus: %s, message: total %d"%(http_status_code, len(data)))
        json_response = {"status": http_status_code, "message": message, "data": data}
        json_response = json.dumps(json_response)
        json_response = json.loads(json_response)
        return json_response
