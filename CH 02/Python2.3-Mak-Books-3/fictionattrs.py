from enum import Enum
from attributes import Attributes

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

class FictionAttrs(Attributes):
    def __init__(self, title, last, first, year, genre):
        super().__init__(title, last, first)
        self._year  = year
        self._genre = genre

    @property
    def year(self): return self._year
    
    @property
    def genre(self): return self._genre
    
    def is_match(self, target_attrs):
        if not super().is_match(target_attrs): return False
        
        return (     
                  (   (target_attrs.year  == 0)
                   or (target_attrs.year  == self._year))
              and   
                  (    (target_attrs.genre == Genre.UNSPECIFIED)
                   or (target_attrs.genre == self._genre))
        )

    def __str__(self):
        return ("{" + super().__str__() + \
                f", YEAR: {self._year} " 
                f", GENRE: {self._genre.name.lower()}" + "}" )
