from time import perf_counter

SIZE = 10_000_000

if __name__ == '__main__':
    lst = []
    
    start_time = perf_counter()
    for i in range(SIZE):
        lst.append(10*i)
    elapsed_time_for_loop = perf_counter() - start_time
        
    print('     for loop elapsed time = '
          f'{elapsed_time_for_loop:6.4f} seconds')
    
    start_time = perf_counter()
    lst = [10*i for i in range(SIZE)]
    elapsed_time_comprehension = perf_counter() - start_time
        
    print('comprehension elapsed time = '
          f'{elapsed_time_comprehension:6.4f} seconds')
    
    print()
    
    improvement = ( 
        (elapsed_time_for_loop - elapsed_time_comprehension)
            /elapsed_time_for_loop
    )
    print(f'{improvement = :4.1%}')
