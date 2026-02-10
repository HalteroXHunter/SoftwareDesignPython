class Automobile:
    def __init__(self):
        self._brakes = []
        self._engine = None
        self._engine_oil = None
        self._heading = None
        self._headlights = []
        self._speed = None
        self._soap = None
        self._tires = []
        self._vacuum_cleaner = None
    
    def accelerate(self):
        print("Accelerating.")
        
    def apply_brakes(self):
        print("Applying brakes.")
        
    def shut_off_engine(self):
        print("Shutting off engine.")
        
    def start_engine(self):
        print("Starting engine.")
        
    def turn_left(self):
        print("Turning left.")
        
    def turn_right(self):
        print("Turning right.")
        
class Garage:
    def __init__(self, car):
        self._car = car
        self._new_oil = None
        self._new_tires = []
        
    def adjust_headlights(self):
        print("Accelerating.")
        
    def change_oil(self):
        print("Changing oil.")
        
    def change_tires(self):
        print("Changing tires.")
        
    def check_brakes(self):
        print("Checking brakes.")
        
    def check_tires(self):
        print("Checking tires.")
        
    def rotate_tires(self):
        print("Rotating tires.")
        
    def tuneup_engine(self):
        print("Tuning up engine.")
    
class CarWash:
    def __init__(self, car):
        self._car = car
        self._vacuum_cleaner = None
        self._wax = None
        
    def vacuum_car(self):
        print("Vacuuming car.")
        
    def wash_car(self):
        print("Washing car.")
        
    def wax_car(self):
        print("Waxing car.")
