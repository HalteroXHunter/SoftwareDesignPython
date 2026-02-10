from baseball_data import BaseballData
from football_info import FootballInfo
from volleyball_stats import VolleyballStats
from attendance_report import AttendanceReport

if __name__ == '__main__':
    baseball_data = BaseballData()
    football_info = FootballInfo()
    volleyball_stats = VolleyballStats()
    
    report = AttendanceReport()
    
    report.print(baseball_data,    'Baseball')
    report.print(football_info,    'Football')
    report.print(volleyball_stats, 'Volleyball')
