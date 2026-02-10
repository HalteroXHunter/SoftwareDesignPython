from enum import Enum

class Genre(Enum):
    UNSPECIFIED = 0
    ADVENTURE   = 1
    CLASSICS    = 2
    DETECTIVE   = 3
    FANTASY     = 4
    HISTORIC    = 5
    HORROR      = 6
    ROMANCE     = 7
    SCIFI       = 8
    
    def __str__(self): return self.name.lower()
