class CircularBuffer:
    
    def _class_invariant(self):
        return (    (0 <= self._head < self._capacity)
                and (0 <= self._tail < self._capacity)
               )
    
    def __init__(self, capacity):
        self._capacity = capacity
        self._head = 0
        self._tail = 0
        self._count = 0
        self._buffer = [0]*capacity
        
        assert self._class_invariant(), \
               'class invariant is false'
        
    @property
    def count(self): return self._count
    
    def add_precondition(self):
        return self._count < self._capacity
    
    def add_postcondition(self):
        return self._count > 0
    
    def add(self, value):
        assert self.add_precondition(), \
               'add_precondition is false'
        
        self._buffer[self._tail] = value
        self._tail = (self._tail + 1)%self._capacity
        self._count += 1
        
        assert self.add_postcondition(), \
               'add_postcondition is false'
        assert self._class_invariant(), \
               'class_invariant is false'

    def remove_precondition(self):
        return self._count > 0
    
    def remove_postcondition(self):
        return self._count < self._capacity
    
    def remove(self):
        assert self.remove_precondition(), \
               'remove_precondition is false'
        
        value = self._buffer[self._head]
        self._head = (self._head + 1)%self._capacity
        self._count -= 1
        
        assert self.remove_postcondition(), \
               'remove_postcondition is false'
        assert self._class_invariant(), \
               'class_invariant is false' 
        
        return value
