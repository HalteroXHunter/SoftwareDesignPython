import math

class Shape:
    def area(self, arg1, arg2=None):
        return (math.pi*arg1*arg1 if arg2 is None
                                  else arg1*arg2
               ) 
