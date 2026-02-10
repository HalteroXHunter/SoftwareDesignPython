N = 4

def solve(n, source, temporary, destination):
    if n == 1:
        print(f'Move {source} ==> {destination}')
    else:
        solve (n - 1, source,    destination, temporary)
        solve (    1, source,    temporary,   destination)
        solve (n - 1, temporary, source,      destination)
        
if __name__ == '__main__':
    solve(N, 'L', 'M', 'R')
