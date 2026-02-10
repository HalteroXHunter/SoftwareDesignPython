from abc import ABC, abstractmethod

class MotorVehicle(ABC):
    def __init__(self):
        self._brakes = []
        self._engine = None
        self._heading = None
        self._speed = 0
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

    def accelerate(self):
        print('vehicle accelerates')
        
    def turn_left(self):
        print('vehicle turns left')
        
    def turn_right(self):
        print('vehicle turns right')
        
    def apply_brakes(self):
        print('vehicle applies brakes')
        
    def drive(self):
        self.start_engine();
        self.accelerate();
        self.turn_left();
        self.turn_right();
        self.apply_brakes();
        self.stop_engine();
