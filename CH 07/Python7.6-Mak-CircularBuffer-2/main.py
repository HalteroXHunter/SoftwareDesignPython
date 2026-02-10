from buffer import CircularBuffer

BUFFER_SIZE = 5

if __name__ == '__main__':
    buffer = CircularBuffer(BUFFER_SIZE)
    
    for value in range(10, 51, 10):
        buffer.add(value)
    
    print(buffer)
    
    buffer[1] = 99
    print(buffer)
    
    print(f'{buffer.remove() = }')
    print(f'{buffer.remove() = }')
    print(buffer)
    
    buffer.pop(1)
    print(buffer)
    