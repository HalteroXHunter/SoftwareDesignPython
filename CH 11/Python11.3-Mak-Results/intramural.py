class Intramural:
    def __init__(self):
        self._sports = []
        self._halls  = []
        
    def add_sport(self, sport):
        self._sports.append(sport)
        
    def add_hall(self, hall):
        self._halls.append(hall)
        
    def print_scores_report(self):
        print()
        print('SCORES REPORT')
        
        for sport in self._sports:
            sport.print_game_scores()
            
    def print_activities_report(self):
        print()
        print('ACTIVITIES REPORT')
        print()
        
        for sport in self._sports:
            sport.print_game_count()
            
    def print_winnings_report(self):
        print()
        print('WINNINGS REPORT')
        print()
        
        for hall in self._halls:
            hall.print_win_count()
    