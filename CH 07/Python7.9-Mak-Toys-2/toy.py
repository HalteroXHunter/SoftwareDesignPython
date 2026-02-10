from abc import ABC, abstractmethod
from playaction import RollPlay, FlyPlay
from sound import EngineSound, ChooChooSound

class Toy(ABC):
    
    @abstractmethod
    def what(self): pass
        
    @abstractmethod
    def play(self): pass
    
    @abstractmethod
    def sound(self): pass

    def __str__(self):
        return (f'{self.what()}\n'
                f'   play: {self.play()}\n'
                f'  sound: {self.sound()}\n'
               )

class ToyCar(Toy, RollPlay, EngineSound):
    def what(self):  return 'TOY CAR'
    def play(self):  return RollPlay.play()
    def sound(self): return EngineSound.sound()

class ModelAirplane(Toy, FlyPlay, EngineSound):
    def what(self):  return 'MODEL AIRPLANE'
    def play(self):  return FlyPlay.play()
    def sound(self): return EngineSound.sound()
    
    def power(self): return 'wind up'
    
    def __str__(self):
        return (   super().__str__()
                 + f'  power: {self.power()}\n'
               )

class TrainSet(Toy, RollPlay, ChooChooSound):
    def what(self):  return 'TRAIN SET'
    def play(self):  return RollPlay.play()
    def sound(self): return ChooChooSound.sound()
     
    def setup(self): return 'lay down track'
    def power(self): return 'insert batteries'
    
    def __str__(self):
        return (   super().__str__()
                 + f'  setup: {self.setup()}\n'
                 + f'  power: {self.power()}\n'
               )
