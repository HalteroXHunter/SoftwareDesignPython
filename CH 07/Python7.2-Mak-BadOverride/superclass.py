class Superclass:
    def operate(self, x: str, y: str): 
        return x + y
    
class Subclass(Superclass):
    def operate(self, x: int, y: int): 
        return x*y
