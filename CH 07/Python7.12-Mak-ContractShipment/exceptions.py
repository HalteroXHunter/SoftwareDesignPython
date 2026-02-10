class CostException(Exception):
    def __init__(self, cost, min_cost):
        self._cost = cost
        self._min_cost = min_cost
        
    @property
    def cost(self): return self._cost
         
    @property
    def min_cost(self): return self._min_cost
    
class DaysException(Exception):
    def __init__(self, days, min_days, max_days):
        self._days = days
        self._min_days = min_days
        self._max_days = max_days
        
    @property
    def days(self): return self._days    
         
    @property
    def min_days(self): return self._min_days
       
    @property
    def max_days(self): return self._max_days
