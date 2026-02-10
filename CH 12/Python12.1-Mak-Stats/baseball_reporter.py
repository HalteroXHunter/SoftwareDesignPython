from event import EventMaker
from log_report import LogReport
from table_report import TableReport
from graph_report import GraphReport

class BaseballReporter:
    def __init__(self):
        self._event_maker  = EventMaker()
        self._log_report   = LogReport()
        self._table_report = TableReport()
        self._graph_report = GraphReport()
        
    def report_hits(self):
        event = self._event_maker.next_event()
        
        while event is not None:
            self._log_report.log_event(event)
            self._table_report.receive_event(event)
            self._graph_report.handle_event(event)
            
            event = self._event_maker.next_event()

        self._log_report.log_event(None)
        self._table_report.receive_event(None)
        self._graph_report.handle_event(None)
