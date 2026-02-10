class CircularBuffer:
    def __init__(self, buffer_size):
        self._buffer_size = buffer_size
        self._head = 0
        self._tail = 0
        self._values_count = 0
        self._buffer = [None]*buffer_size
        
    @property
    def values_count(self): return self._values_count

    def add(self, value):
        self._buffer[self._tail] = value
        self._tail = (self._tail + 1)%self._buffer_size
        self._values_count += 1
    
    def remove(self):
        value = self._buffer[self._head]
        self._head = (self._head + 1)%self._buffer_size
        self._values_count -= 1
        
        return value
    
    def __str__(self):
        i = self._head
        c = self._values_count
        
        result = 'Contents:'
        
        while c > 0:
            result += f' {self._buffer[i]}'
            i = (i + 1)%self._buffer_size
            c -= 1
            
        return result
