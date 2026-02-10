from motorvehicleinterface import MotorVehicleInterface

class Car(MotorVehicleInterface):
    def __init__(self):
        self._brakes = []
        self._engine = None
        self._heading = None
        self._speed = 0
    
    def start_engine(self):
        print('car starts engine')
    
    def stop_engine(self):
        print('car stops engine')

    def accelerate(self):
        print('car accelerates')
        
    def turn_left(self):
        print('car turns left')
        
    def turn_right(self):
        print('car turns right')
        
    def apply_brakes(self):
        print('car applies brakes')
        
    def drive(self):
        self.start_engine();
        self.accelerate();
        self.turn_left();
        self.turn_right();
        self.apply_brakes();
        self.stop_engine();
