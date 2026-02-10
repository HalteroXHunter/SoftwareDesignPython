from game_data import GameData
from volleyball_stats import VolleyballStats

class VolleyballData(GameData, VolleyballStats):
    def report_venue(self):
        return self._stats['venue']
    
    def report_attendance(self):
        return self._stats['attendance']
