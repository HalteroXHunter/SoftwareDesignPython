from enum import Enum
from exceptions import CostException, DaysException

class ShipmentKind(Enum):
    REGULAR       = 1
    EXPEDITED     = 2
    INTERNATIONAL = 3
    
    def __str__(self): return self.name
    
class Shipment:
    _min_cost = 1
    _min_days = 1
    _max_days = 14
    
    def __init__(self):
        self._cost = 0
        self._days = 0
        self._calculated_days = 5
        
    @property
    def kind(self): return ShipmentKind.REGULAR
    
    @property
    def cost(self): return self._cost
    
    @property
    def days(self): return self._calculated_days
    
    @cost.setter
    def cost(self, cost):
        # precondition
        if cost >= self._min_cost:
            self._cost = cost
        else:
            raise CostException(cost, self._min_cost)
    
    def calculate_days(self):
        self._days = self._calculated_days
        print(f'  calculated days = {self._days}')
        
        # postcondition
        if not (self._min_days <= self._days 
                               <= self._max_days):
            raise DaysException(self._days, self._min_days, 
                                            self._max_days)
