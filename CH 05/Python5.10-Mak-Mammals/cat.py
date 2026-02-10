from mammal import Mammal

class Cat(Mammal):
    def __init__(self, weight, height, fur_factor):
        super().__init__(weight, height)
        self._fur_factor = fur_factor

    def _shed(self):
        if self._fur_factor > 1.0:
            print('shed a lot')
        else:
            print('shed a little')
            
    def eat(self):
        print('eat from a bowl')
        
    def perform(self):
        self._shed()
