SIZE = 5

def reverse(v):
    if len(v) == 1:
        return v[0]
    
    first_value = v[0]
    v.pop(0)
    reverse(v)
    
    return v.append(first_value)
    
if __name__ == '__main__':
    data = [ 10*i for i in range(SIZE + 1)]
    print(f'Reverse of {data}')
    
    reverse(data)
    print(f'        is {data}')
