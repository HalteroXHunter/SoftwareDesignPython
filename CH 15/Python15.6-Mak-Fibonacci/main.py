def f(n):
    if n < 2:
        return n
    else:
        return f(n - 2) + f(n - 1)
    
if __name__ == '__main__':
    print('  n        f[n]')
    print('---------------')
    
    for n in range(51):
        print(f'{n:3d} {f(n):11d}')
