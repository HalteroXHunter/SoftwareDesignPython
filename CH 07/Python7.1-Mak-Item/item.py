class Item:
    def __init__(self, name):
        self._name = name
        
    def _cost(self, regular_price, weight):
        return regular_price*weight
        
    def print_cost(self, regular_price, weight):
        print(f'The total cost of {self._name} '
              f'is ${regular_price:.2f}/lb')
        print(f'  times ${weight:.1f} lbs '
              f'= ${self._cost(regular_price, weight):.2f}')
        
class OrganicItem(Item):
    def __init__(self, name, markup):
        super().__init__(name)
        self._markup = markup
        
    def _cost(self, organic_price, weight):
        markup_factor = 1 + self._markup/100;
        return super()._cost(organic_price, weight)*markup_factor
    
    def print_cost(self, organic_price, weight):
        print(f'The total cost of organic {self._name} '
              f'is ${organic_price:.2f}/lb')
        print(f'  times ${weight:.1f} lbs '
              f'= ${super()._cost(organic_price, weight):.2f} '
              f'+ {self._markup}% extra '
              f'= ${self._cost(organic_price, weight):.2f}')
