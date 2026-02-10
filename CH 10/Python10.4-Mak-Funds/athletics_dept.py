from alumni import Alumni
from booster_clubs import BoosterClubs
from students import Students

class AthleticsDept:
    def raise_funds(self):
        alumni = Alumni()
        clubs = BoosterClubs()
        students = Students()

        print()
        print('ATHLETICS DEPARTMENT')
        
        alumni.send_solicitations()
        clubs.schedule_meetings()
        students.collect_fees()
