from abc import ABC, abstractmethod

class PlayAction(ABC):
    
    @staticmethod
    @abstractmethod
    def play(self): pass
    
class RollPlay(PlayAction):
    
    @staticmethod
    def play(): return 'roll it'
    
class FlyPlay(PlayAction):
    
    @staticmethod
    def play(): return 'fly it'
    