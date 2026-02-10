import random

class ExecutivePass:
    def __init__(self):
        self._key = random.randint(1, 999)
        self._holder = None
        
        print("** Executive pass created, "
              f"key = {self._key}")
        print()
    
    def __str__(self):
        return (f'pass holder is {self._holder}, '
                f'key = {self._key}')

    def obtain(self, holder):
        self._holder = holder
        return self
