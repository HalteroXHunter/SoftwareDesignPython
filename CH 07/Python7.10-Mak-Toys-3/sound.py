from abc import ABC, abstractmethod

class Sound(ABC):
    
    @staticmethod
    @abstractmethod
    def sound(): pass
    
class EngineSound(Sound):
    
    @staticmethod
    def sound(): return 'RRrr RRrr'
    
class ChooChooSound(Sound):
    
    @staticmethod
    def sound(): return 'choo choo'
    