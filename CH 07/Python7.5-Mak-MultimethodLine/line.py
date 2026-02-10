import math
from multimethod import multimethod
from point import Point
          
class Line:
    @staticmethod
    def _pythagoras(x1: float, y1: float, 
                    x2: float, y2: float) -> float:
        d1 = x1 - x2
        d2 = y1 - y2
        return math.hypot(d1, d2)
    
    @multimethod
    def length(self, x1: float, y1: float, 
                     x2: float, y2: float) -> float:
        return Line._pythagoras(x1, y1, x2, y2)
    
    @multimethod
    def length(self, coordinates: list) -> float: 
        x1, y1, x2, y2 = coordinates
        return Line._pythagoras(x1, y1, x2, y2)
        
    @multimethod
    def length(self, point1: dict, point2: dict) -> float:
        x1 = point1['x']
        y1 = point1['y']
        x2 = point2['x']
        y2 = point2['y']
        return Line._pythagoras(x1, y1, x2, y2)
    
    @multimethod
    def length(self, point1: Point, point2: Point) -> float:
        x1 = point1.x
        y1 = point1.y
        x2 = point2.x
        y2 = point2.y
        return Line._pythagoras(x1, y1, x2, y2)
        
    @multimethod
    def length(self, point1: tuple, point2: tuple) -> float:
        x1, y1 = point1
        x2, y2 = point2
        return Line._pythagoras(x1, y1, x2, y2)
