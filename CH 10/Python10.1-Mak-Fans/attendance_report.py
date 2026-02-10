from multimethod import multimethod

from game_data import GameData
from baseball_data import BaseballData
from football_info import FootballInfo
from volleyball_stats import VolleyballStats

class AttendanceReport: 
    class _ConvertedData(GameData):
        def __init__(self, venue, attendance):
            self._venue = venue
            self._attendance = attendance
            
        def report_venue(self):
            return self._venue
        
        def report_attendance(self):
            return self._attendance
        
    def legacy_print(self, game_data, title):
        print(title)
        print(f'  {game_data.report_venue()}: ', end='')
        print(f'{game_data.report_attendance()}')
        print()
    
    @multimethod
    def print(self, data: BaseballData, title):
        self.legacy_print(data, title)
            
    @multimethod
    def print(self, data: FootballInfo, title):
        venue = data.info[0]
        attendance = data.info[1]
        self.legacy_print(self._ConvertedData(venue, attendance), 
                          title)
            
    @multimethod
    def print(self, data: VolleyballStats, title):
        venue = data.stats['venue']
        attendance = data.stats['attendance']
        self.legacy_print(self._ConvertedData(venue, attendance),
                          title)
