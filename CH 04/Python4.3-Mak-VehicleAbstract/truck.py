from motorvehicle import MotorVehicle

class Truck(MotorVehicle):
    def start_engine(self):
        print('truck starts engine')
    
    def stop_engine(self):
        print('truck stops engine')
        
    def turn_left(self):
        print('truck turns left')
        
    def turn_right(self):
        print('truck turns right')
