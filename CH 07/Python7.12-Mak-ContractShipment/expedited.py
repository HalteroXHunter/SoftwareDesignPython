from shipment import ShipmentKind, Shipment

class Expedited(Shipment):
    _min_cost = 5
    _min_days = 1
    _max_days = 3
    
    def __init__(self):
        self._cost = 0
        self._calculated_days = 2
    
    @property
    def kind(self): return ShipmentKind.EXPEDITED
