from sport import Category, SportType, Sport
from player_strategy import VarsityBaseballPlayers, \
                            VarsityFootballPlayers, \
                            IntramuralBaseballPlayers, \
                            IntramuralFootballPlayers, \
                            IntramuralVolleyballPlayers
from venue_strategy import Stadium, OpenField

class VarsityBaseball(Sport):
    _CATEGORY = Category.VARSITY
    _SPORT_TYPE = SportType.BASEBALL
        
    def __init__(self):
        super().__init__(VarsityBaseballPlayers(),
                         Stadium())

class VarsityFootball(Sport):
    _CATEGORY = Category.VARSITY
    _SPORT_TYPE = SportType.FOOTBALL
        
    def __init__(self):
        super().__init__(VarsityFootballPlayers(),
                         Stadium())

class IntramuralBaseball(Sport):
    _CATEGORY = Category.INTRAMURAL
    _SPORT_TYPE = SportType.BASEBALL
        
    def __init__(self):
        super().__init__(IntramuralBaseballPlayers(),
                         OpenField())

class IntramuralFootball(Sport):
    _CATEGORY = Category.INTRAMURAL
    _SPORT_TYPE = SportType.FOOTBALL
        
    def __init__(self):
        super().__init__(IntramuralFootballPlayers(),
                         OpenField())

class IntramuralVolleyball(Sport):
    _CATEGORY = Category.INTRAMURAL
    _SPORT_TYPE = SportType.VOLLEYBALL
        
    def __init__(self):
        super().__init__(IntramuralVolleyballPlayers(),
                         OpenField())
