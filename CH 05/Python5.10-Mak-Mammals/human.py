from mammal import Mammal

class Human(Mammal):
    def __init__(self, weight, height, needs_glasses):
        super().__init__(weight, height)
        self._needs_glasses = needs_glasses
        
    def _read_book(self):
        if self._needs_glasses:
            print('squint')
        print('turn pages')
            
    def eat(self): 
        print('eat with knife and fork')
        
    def perform(self):
        self._read_book()
        self.sleep()
        