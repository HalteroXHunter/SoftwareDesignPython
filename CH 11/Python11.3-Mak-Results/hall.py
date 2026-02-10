from enum import Enum

class HallName(Enum):
    NORTH = 1
    SOUTH = 2
    EAST  = 3
    WEST  = 4
    
    def __str__(self): 
        return (self.name.lower().capitalize() + ' Hall')

class Hall:
    def __init__(self, name):
        self._name = name
        self._win_count = 0
        
    @property
    def name(self):
        return self._name
        
    def increment_win_count(self):
        self._win_count += 1
        
    def print_win_count(self):
        print(f'{self._name:>12s} won '
              f'{self._win_count} game(s)')
