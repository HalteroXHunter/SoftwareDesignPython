from alumni import Alumni
from booster_clubs import BoosterClubs
from students import Students

class Administration:
    def aid_fundraising(self):
        alumni = Alumni()
        clubs = BoosterClubs()
        students = Students()

        print()
        print('SCHOOL ADMINISTRATION')
        
        alumni.send_solicitations()
        clubs.schedule_meetings()
        students.collect_fees()
