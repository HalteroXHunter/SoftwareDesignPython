class Driver:
    def __init__(self, c):
        self._car = c
        
    def start_car(self):
        self._car.step_on_brake()
        self._car.insert_key()
        self._car.turn_key()
        self._car.step_on_accelerator()
        