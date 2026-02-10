import math
from point import Point

class Line:
    def length(self, *args):
        argslen = len(args)
        
        if argslen == 1:
            x1, y1, x2, y2 = args[0]
            
        elif argslen == 2:
            arg1, arg2 = args
            
            if type(arg1) is dict:
                x1 = arg1['x']
                y1 = arg1['y']
            elif type(arg1) is Point:
                x1 = arg1.x
                y1 = arg1.y
            else:  # arg1 is list or tuple
                x1, y1 = arg1
                
            if type(arg2) is dict:
                x2 = arg2['x']
                y2 = arg2['y']
            elif type(arg2) is Point:
                x2 = arg2.x
                y2 = arg2.y
            else:  # arg2 is list or tuple
                x2, y2 = arg2
                
        elif argslen == 4:
            x1, y1, x2, y2 = args
            
        else:
            raise Exception(f'Unsupported arguments: {args}')
            
        d1 = x1 - x2
        d2 = y1 - y2
        
        return math.hypot(d1, d2)
