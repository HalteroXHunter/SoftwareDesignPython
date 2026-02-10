from enum import Enum

class Region(Enum):
    UNSPECIFIED = 0
    China       = 1
    France      = 2
    India       = 3
    Italy       = 4
    Mexico      = 5
    Persia      = 6
    US          = 7
    
    def __str__(self): return self.name
