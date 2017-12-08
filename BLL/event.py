from DAL.event import Event as EventDAL

event = EventDAL()
class Event():
    def parse_data_row_as_json_fortmat(self, event_monitor):
        agrs = {
            'id'                    : event_monitor[0],
            'event_name'            : event_monitor[1],
            'start_date'            : str(event_monitor[2]),
            'end_date'              : str(event_monitor[3]),
            'encoder'               : event_monitor[4],
            'service_check_id'      : event_monitor[5],
            'service_check_name'    : event_monitor[6],
            'ip_monitor'            : event_monitor[7],
            'source_main'           : event_monitor[8],
            'source_backup'         : event_monitor[9],
            'status'                : event_monitor[10],
            'last_update'           : str(event_monitor[11]),
            'active'                : event_monitor[12]
        }
        return agrs
        
    def get_event_monitor_list(self):
        event_monitor_list = event.get_event_monitor_list()
        agrs = []
        for event_monitor in event_monitor_list:
            agrs.append(self.parse_data_row_as_json_fortmat(event_monitor))
        return agrs

    def get_running_event_monitor_list(self):
        event_monitor_list = event.get_running_event_monitor_list()
        agrs = []
        for event_monitor in event_monitor_list:
            agrs.append(self.parse_data_row_as_json_fortmat(event_monitor))
        return agrs

    def get_waiting_event_monitor_list(self):
        event_monitor_list = event.get_waiting_event_monitor_list()
        agrs = []
        for event_monitor in event_monitor_list:
            agrs.append(self.parse_data_row_as_json_fortmat(event_monitor))
        return agrs

    def get_completed_event_monitor_list(self):
        event_monitor_list = event.get_completed_event_monitor_list()
        agrs = []
        for event_monitor in event_monitor_list:
            agrs.append(self.parse_data_row_as_json_fortmat(event_monitor))
        return agrs

    def get_event_monitor(self, pk):
        event_monitor_list = event.get_event_monitor(pk)
        agrs = []
        agrs.append(self.parse_data_row_as_json_fortmat(event_monitor_list[0]))
        return agrs