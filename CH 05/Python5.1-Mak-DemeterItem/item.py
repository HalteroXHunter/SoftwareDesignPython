class Item:
    def __init__(self, name, weight, price):        
        # Private attributes
        self._name = name
        self._weight = weight
        self._price = price
        
    @property
    def name(self): return self._name
    
    @property
    def weight(self): return self._weight
    
    @property
    def price(self): return self._price
    
    @price.setter
    def price(self, new_price):
        assert new_price > 0
        self._price = new_price
        