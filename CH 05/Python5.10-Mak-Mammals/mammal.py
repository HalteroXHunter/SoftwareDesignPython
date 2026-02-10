from abc import abstractmethod

class Mammal:
    def __init__(self, weight, height):
        self.__weight = weight
        self.__height = height
        
    @property
    def weight(self): return self.__weight
    
    @property
    def height(self): return self.__height
    
    def _snore(self):
        print('Zzzz')
        
    @abstractmethod
    def eat(self): 
        pass
    
    @abstractmethod
    def perform(self): 
        pass
    
    def sleep(self):
        print('close eyes')
        self._snore()