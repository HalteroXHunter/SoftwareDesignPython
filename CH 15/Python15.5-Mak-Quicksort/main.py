from random import randint
from quicksort import Quicksort

SIZE = 20

if __name__ == '__main__':
    data = [ randint(0, SIZE - 1) for _ in range(SIZE)]
    
    qsorter = Quicksort(data)
    
    print(f'Before: {data}')
    qsorter.sort()
    print(f' After: {data}')
    
    print()
    if qsorter.verify_sorted():
        print('Successfully sorted!')
    else:
        print('*** FAILED ***')
