from sport import Sport

class Baseball(Sport):
    _SPORT_TYPE = 'BASEBALL'
        
    def recruit_players(self):
        return 'baseball players'
    
    def reserve_venue(self):
        return 'stadium'

class Football(Sport):
    _SPORT_TYPE = 'FOOTBALL'
        
    def recruit_players(self):
        return 'football players'
    
    def reserve_venue(self):
        return 'stadium'

class Volleyball(Sport):
    _SPORT_TYPE = 'VOLLEYBALL'
        
    def recruit_players(self):
        return 'volleyball players'
    
    def reserve_venue(self):
        return 'open field'
