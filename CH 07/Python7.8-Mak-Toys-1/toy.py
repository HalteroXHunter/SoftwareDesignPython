from abc import ABC, abstractmethod

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

class ToyCar(Toy):
    def what(self):  return 'TOY CAR'
    def play(self):  return 'roll it'
    def sound(self): return 'RRrr RRrr'

class ModelAirplane(Toy):
    def what(self):  return 'MODEL AIRPLANE'
    def play(self):  return 'fly it'
    def sound(self): return 'RRrr RRrr'
    
    def power(self): return 'wind up'
    
    def __str__(self):
        return (   super().__str__()
                 + f'  power: {self.power()}\n'
               )

class TrainSet(Toy):
    def what(self):  return 'TRAIN SET'
    def play(self):  return 'roll it'
    def sound(self): return 'choo choo'
     
    def setup(self): return 'lay down track'
    def power(self): return 'insert batteries'
    
    def __str__(self):
        return (   super().__str__()
                 + f'  setup: {self.setup()}\n'
                 + f'  power: {self.power()}\n'
               )
