class Book:
    def __init__(self, attributes):
        self._attributes = attributes

    @property
    def attributes(self): return self._attributes
    
    def __str__(self):
        return str(self._attributes)