from baseball_data import BaseballData
from football_data import FootballData
from volleyball_data import VolleyballData
from attendance_report import AttendanceReport

if __name__ == '__main__':
    baseball_data = BaseballData()
    football_data = FootballData()
    volleyball_data = VolleyballData()
    
    report = AttendanceReport()
    
    report.legacy_print(baseball_data,   'Baseball')
    report.legacy_print(football_data,   'Football')
    report.legacy_print(volleyball_data, 'Volleyball')
