from MySQL_Database import Database

class Event():
    def __init__(self):
        self.db = Database()

    def get_event_monitor_list(self, region = None):
        if region:
            sql = """select evm.id, evm.pid, ev.name as event_name, ev.start_date, ev.end_date, en.name as encoder, svc.id as service_check_id, svc.name as service_check_name, en.ip_monitor, en.source_main, en.source_backup, evm.status, evm.last_update, evm.active
                from event_monitor as evm, event as ev, encoder as en, service_check as svc 
                where ev.active = 1 and ev.region = '%s' and evm.active = 1 and en.active = 1 and svc.active = 1 and evm.event_id = ev.id and evm.encoder_id = en.id and evm.service_check_id = svc.id
                ORDER BY ev.start_date DESC"""%(region) 
        else:
            sql = """select evm.id, evm.pid, ev.name as event_name, ev.start_date, ev.end_date, en.name as encoder, svc.id as service_check_id, svc.name as service_check_name, en.ip_monitor, en.source_main, en.source_backup, evm.status, evm.last_update, evm.active
                from event_monitor as evm, event as ev, encoder as en, service_check as svc 
                where ev.active = 1 and evm.active = 1 and en.active = 1 and svc.active = 1 and evm.event_id = ev.id and evm.encoder_id = en.id and evm.service_check_id = svc.id
                ORDER BY ev.start_date DESC"""
        status, message, data_table = self.db.execute_query(sql)
        return data_table

    def get_running_event_monitor_list(self, region = None):
        if region:
            sql ="""select evm.id, evm.pid, ev.name as event_name, ev.start_date, ev.end_date, en.name as encoder, svc.id as service_check_id, svc.name as service_check_name, en.ip_monitor, en.source_main, en.source_backup, evm.status, evm.last_update, evm.active
                from event_monitor as evm, event as ev, encoder as en, service_check as svc 
                where ev.start_date < unix_timestamp(now()) and ev.end_date > unix_timestamp(now()) and ev.active = 1 and ev.region = '%s' and evm.active = 1 and en.active = 1 and svc.active = 1 and evm.event_id = ev.id and evm.encoder_id = en.id and evm.service_check_id = svc.id
                ORDER BY ev.start_date DESC"""%("HCM") 
        else:
            sql = """select evm.id, evm.pid, ev.name as event_name, ev.start_date, ev.end_date, en.name as encoder, svc.id as service_check_id, svc.name as service_check_name, en.ip_monitor, en.source_main, en.source_backup, evm.status, evm.last_update, evm.active
                from event_monitor as evm, event as ev, encoder as en, service_check as svc 
                where ev.start_date < unix_timestamp(now()) and ev.end_date > unix_timestamp(now()) and ev.active = 1 and evm.active = 1 and en.active = 1 and svc.active = 1 and evm.event_id = ev.id and evm.encoder_id = en.id and evm.service_check_id = svc.id
                ORDER BY ev.start_date DESC"""
        status, message, data_table = self.db.execute_query(sql)
        return data_table

    def get_waiting_event_monitor_list(self, region = None):
        if region:
            sql = """select evm.id, evm.pid, ev.name as event_name, ev.start_date, ev.end_date, en.name as encoder, svc.id as service_check_id, svc.name as service_check_name, en.ip_monitor, en.source_main, en.source_backup, evm.status, evm.last_update, evm.active
                from event_monitor as evm, event as ev, encoder as en, service_check as svc 
                where ev.start_date > unix_timestamp(now()) and ev.end_date > unix_timestamp(now()) and ev.active = 1 and ev.region = '%s' and evm.active = 1 and en.active = 1 and svc.active = 1 and evm.event_id = ev.id and evm.encoder_id = en.id and evm.service_check_id = svc.id
                ORDER BY ev.start_date DESC"""%(region) 
        else:
            sql = """select evm.id, evm.pid, ev.name as event_name, ev.start_date, ev.end_date, en.name as encoder, svc.id as service_check_id, svc.name as service_check_name, en.ip_monitor, en.source_main, en.source_backup, evm.status, evm.last_update, evm.active
                from event_monitor as evm, event as ev, encoder as en, service_check as svc 
                where ev.start_date > unix_timestamp(now()) and ev.end_date > unix_timestamp(now()) and ev.active = 1 and evm.active = 1 and en.active = 1 and svc.active = 1 and evm.event_id = ev.id and evm.encoder_id = en.id and evm.service_check_id = svc.id
                ORDER BY ev.start_date DESC"""
        status, message, data_table = self.db.execute_query(sql)
        return data_table

    def get_completed_event_monitor_list(self, region = None):
        if region:
            sql = """select evm.id, evm.pid, ev.name as event_name, from_unixtime(ev.start_date), from_unixtime(ev.end_date), en.name as encoder, svc.id as service_check_id, svc.name as service_check_name, en.ip_monitor, en.source_main, en.source_backup, evm.status, evm.last_update, evm.active
                from event_monitor as evm, event as ev, encoder as en, service_check as svc 
                where ev.start_date < unix_timestamp(now()) and ev.end_date < unix_timestamp(now()) and ev.active = 1 and ev.region = '%s' and evm.active = 1 and en.active = 1 and svc.active = 1 and evm.event_id = ev.id and evm.encoder_id = en.id and evm.service_check_id = svc.id
                ORDER BY ev.start_date DESC"""%(region) 
        else:
            sql = """select evm.id, evm.pid, ev.name as event_name, from_unixtime(ev.start_date), from_unixtime(ev.end_date), en.name as encoder, svc.id as service_check_id, svc.name as service_check_name, en.ip_monitor, en.source_main, en.source_backup, evm.status, evm.last_update, evm.active
                from event_monitor as evm, event as ev, encoder as en, service_check as svc 
                where ev.start_date < unix_timestamp(now()) and ev.end_date < unix_timestamp(now()) and ev.active = 1 and evm.active = 1 and en.active = 1 and svc.active = 1 and evm.event_id = ev.id and evm.encoder_id = en.id and evm.service_check_id = svc.id
                ORDER BY ev.start_date DESC"""
        status, message, data_table = self.db.execute_query(sql)
        return data_table

    def get_event_monitor(self, pk):
        sql = """select evm.id, evm.pid, ev.name as event_name, ev.start_date, ev.end_date, en.name as encoder, svc.id as service_check_id, svc.name as service_check_name, en.ip_monitor, en.source_main, en.source_backup, evm.status, evm.last_update, evm.active
                from event_monitor as evm, event as ev, encoder as en, service_check as svc 
                where evm.id = %d and ev.active = 1 and evm.active = 1 and en.active = 1 and svc.active = 1 and evm.event_id = ev.id and evm.encoder_id = en.id and evm.service_check_id = svc.id
                ORDER BY ev.start_date DESC"""%(int(pk))
        status, message, data_table = self.db.execute_query(sql)
        return data_table

    def update_last_update(self, pk):
        sql = """update event_monitor set last_update = unix_timestamp(now()) where id = %d"""%(int(pk))
        status, message, data_table = self.db.execute_non_query(sql)
        return status