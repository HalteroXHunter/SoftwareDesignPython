from random import randint

SIZE = 12

def largest(v):
    if len(v) == 1:
        return v[0]
    
    first_value = v[0]
    v.pop(0)
    largest_of_rest = largest(v)
    
    return first_value if first_value > largest_of_rest \
                       else largest_of_rest
    
if __name__ == '__main__':
    data = [ randint(0, 100) for _ in range(SIZE) ]
    print(f'Largest of {data}')
    print(f'is {largest(data)}')
