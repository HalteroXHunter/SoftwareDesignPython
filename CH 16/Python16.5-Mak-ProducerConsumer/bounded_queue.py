from threading import Condition

class BoundedQueue(object):
    def __init__(self, capacity):
        self._capacity = capacity
        self._data = []
        self._condition = Condition()
        
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def condition(self):
        return self._condition
    
    @property
    def data(self):
        return self._data
    
    def size(self):
        return len(self._data)
    
    def enter(self, value):
        self._data.append(value)
        
    def remove(self):
        return self._data.pop(0)
    
    def peek(self):
        return None if self.is_empty() else self.data[0]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def is_full(self):
        return len(self.data) == self._capacity
    
    def just_became_not_empty(self):
        return len(self._data) == 1
    
    def just_became_not_full(self):
        return len(self._data) == self._capacity - 1
    