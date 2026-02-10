class ProvisionItem:
    def __init__(self, name, cost):
        self._name = name
        self._cost = cost
    
    @property
    def name(self):
        return self._name
    
    @property
    def cost(self):
        return self._cost
       
    def print_item(self):
        print(f'{self._name:>6s} cost: ${self.cost:2d}')
    
