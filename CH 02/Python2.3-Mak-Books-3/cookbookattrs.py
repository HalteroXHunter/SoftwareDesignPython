from enum import Enum
from attributes import Attributes

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

class CookbookAttrs(Attributes):
    def __init__(self, title, last, first, region):
        super().__init__(title, last, first)
        self._region = region
        
    @property
    def region(self): return self._region
    
    def is_match(self, target_attrs):
        if not super().is_match(target_attrs): return False
        
        return (   (target_attrs.region == Region.UNSPECIFIED)
                or (target_attrs.region == self._region))

    def __str__(self):
        return ("{" + super().__str__() + \
                f", REGION: {self._region}" + "}")
