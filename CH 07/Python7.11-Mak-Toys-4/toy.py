from abc import ABC, abstractmethod

class Toy(ABC):
    def __init__(self, play, sound):
        self.__play = play
        self.__sound = sound
    
    @abstractmethod
    def what(self): pass
    
    @property
    def play(self):
        return self.__play.play()
        
    @property
    def sound(self):
        return self.__sound.sound()
    
    @play.setter
    def play(self, play):
        self.__play = play
        
    @sound.setter
    def sound(self, sound):
        self.__sound = sound

    def __str__(self):
        return (f'{self.what()}\n'
                f'   play: {self.__play.play()}\n'
                f'  sound: {self.__sound.sound()}\n'
               )

class ToyCar(Toy):
    def __init__(self, play, sound):
        super().__init__(play, sound)
    
    def what(self):  return 'TOY CAR'

class ModelAirplane(Toy):
    def __init__(self, play, sound):
        super().__init__(play, sound)
    
    def what(self):  return 'MODEL AIRPLANE'    
    def power(self): return 'wind up'
    
    def __str__(self):
        return (   super().__str__()
                 + f'  power: {self.power()}\n'
               )

class TrainSet(Toy):
    def __init__(self, play, sound):
        super().__init__(play, sound)
    
    def what(self):  return 'TRAIN SET'
    def setup(self): return 'lay down track'
    def power(self): return 'insert batteries'
    
    def __str__(self):
        return (   super().__str__()
                 + f'  setup: {self.setup()}\n'
                 + f'  power: {self.power()}\n'
               )
