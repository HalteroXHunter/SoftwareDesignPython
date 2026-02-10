from abc import ABC, abstractmethod

class MotorVehicleInterface(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass
        
    @abstractmethod
    def turn_left(self):
        pass
        
    @abstractmethod
    def turn_right(self):
        pass
        
    @abstractmethod
    def apply_brakes(self):
        pass
        
    @abstractmethod
    def drive(self):
        pass
