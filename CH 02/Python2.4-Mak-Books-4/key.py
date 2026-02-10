from enum import Enum

class Key(Enum):
    KIND    = 0
    TITLE   = 1
    LAST    = 2
    FIRST   = 3
    YEAR    = 4
    GENRE   = 5
    REGION  = 6
    SUBJECT = 7
    
    def __str__(self): return self.name