from abc import ABC, abstractmethod

class Sport(ABC):
    _SPORT_TYPE = ''
        
    @property
    def SPORT_TYPE(self): return self._SPORT_TYPE
    
    @abstractmethod
    def recruit_players(self): pass
    
    @abstractmethod
    def reserve_venue(self): pass
