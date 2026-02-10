from buffer import CircularBuffer

SIZE = 5

if __name__ == '__main__':
    buffer = CircularBuffer(SIZE)
    
    for value in range(10, 101, 10):
        if buffer.add_precondition():
            buffer.add(value)
            print(f'added {value}')
            
    for _ in range(10):
        if buffer.remove_precondition():
            value = buffer.remove()
            print(f'removed {value}')

    buffer.remove()
