from game_data import GameData
from football_info import FootballInfo

class FootballData(GameData, FootballInfo):
    def report_venue(self):
        return self._info[0]
    
    def report_attendance(self):
        return self._info[1]
