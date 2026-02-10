from motorvehicleinterface import MotorVehicleInterface

class Truck(MotorVehicleInterface):
    def __init__(self):
        self._brakes = []
        self._engine = None
        self._heading = None
        self._speed = 0
    
    def start_engine(self):
        print('truck starts engine')
    
    def stop_engine(self):
        print('truck stops engine')

    def accelerate(self):
        print('truck accelerates')
        
    def turn_left(self):
        print('truck turns left')
        
    def turn_right(self):
        print('truck turns right')
        
    def apply_brakes(self):
        print('truck applies brakes')
        
    def drive(self):
        self.start_engine();
        self.accelerate();
        self.turn_left();
        self.turn_right();
        self.apply_brakes();
        self.stop_engine();
