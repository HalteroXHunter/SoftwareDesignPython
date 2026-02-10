from shipment import ShipmentKind, Shipment

class International(Shipment):
    _min_cost = 10
    _min_days = 7
    _max_days = 21
        
    def __init__(self):
        self._cost = 0
        self._calculated_days = 20

    @property
    def kind(self): return ShipmentKind.INTERNATIONAL
