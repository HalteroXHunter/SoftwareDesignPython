from enum import Enum

class Kind(Enum):
    FICTION  = 0
    COOKBOOK = 1
    HOWTO    = 2
    
    def __str__(self): return self.name.lower()
