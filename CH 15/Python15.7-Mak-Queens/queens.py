class Queens(object):
    _SIZE = 8
    
    def __init__(self):
        self._count = 0
        self._occupied = [ [False]*Queens._SIZE 
                           for _ in range(Queens._SIZE) 
                         ]
    
    def _print_board(self):
        self._count += 1
        
        print()
        print(f'Solution #{self._count}')
        print()
        
        for row in range(Queens._SIZE):
            for col in range(Queens._SIZE):
                piece = 'Q ' if self._occupied[row][col] \
                        else '. '
                print(piece, end='')
            print()
        
    def find_solutions(self):
        self._find_solutions(0)
        
    def _find_solutions(self, col):
        for row in range(Queens._SIZE):
            if self._is_safe_position(row, col):
                self._occupied[row][col] = True
                
                if col == Queens._SIZE - 1:
                    self._print_board()
                else:
                    self._find_solutions(col + 1)
                    
            self._occupied[row][col] = False
            
    def _is_safe_position(self, row, col):
        for c in range(0, col):
            if self._occupied[row][c]:
                return False
            
        r = row - 1
        c = col - 1
        
        while r >= 0 and c >= 0:
            if self._occupied[r][c]:
                return False
            r -= 1
            c -= 1
            
        r = row + 1
        c = col - 1
        
        while r < Queens._SIZE and c >= 0:
            if self._occupied[r][c]:
                return False
            r += 1
            c -= 1
            
        return True
