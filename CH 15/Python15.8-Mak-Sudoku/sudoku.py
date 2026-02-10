class Sudoku(object):
    _BLOCK_SIZE = 3
    _GRID_SIZE  = _BLOCK_SIZE*_BLOCK_SIZE
    
    def __init__(self, file_name):
        self._grid = []
        
        with open(file_name, 'r') as elements:
            for line in elements:
                if len(line) > 1:
                    row = line.split()
                    for i in range(len(row)):
                        row[i] = int(row[i])
                    self._grid.append(row)
        
    def print_grid(self):
        for row in range(Sudoku._GRID_SIZE):
            if row > 0 and row%Sudoku._BLOCK_SIZE == 0:
                print('------+-------+-------')
                
            for col in range(Sudoku._GRID_SIZE):
                if col > 0 and col%Sudoku._BLOCK_SIZE == 0:
                    print('| ', end='')
                    
                g = self._grid[row][col]
                if g > 0:
                    print(f'{g} ', end='')
                else:
                    print('. ', end='')
                        
            print()

    def solve(self):
        return self._solve(0, 0)
    
    def _solve(self, row, col):
        if (    row == Sudoku._GRID_SIZE - 1
            and col == Sudoku._GRID_SIZE):
            return True;
        
        if col == Sudoku._GRID_SIZE:
            row += 1
            col = 0
            
        if self._grid[row][col] != 0:
            return self._solve(row, col + 1)
        
        for number in range(1, Sudoku._GRID_SIZE + 1):
            if self._is_number_valid(row, col, number):
                self._grid[row][col] = number
                
                if self._solve(row, col + 1):
                    return True
                
        self._grid[row][col] = 0
        return False
    
    def _is_number_valid(self, row, col, number):
        for c in range(Sudoku._GRID_SIZE):
            if self._grid[row][c] == number:
                return False
            
        for r in range(Sudoku._GRID_SIZE):
            if self._grid[r][col] == number:
                return False
            
        block_row_start = row - row%Sudoku._BLOCK_SIZE;
        block_col_start = col - col%Sudoku._BLOCK_SIZE;
        block_row_end = block_row_start + Sudoku._BLOCK_SIZE;
        block_col_end = block_col_start + Sudoku._BLOCK_SIZE;
        
        for r in range(block_row_start, block_row_end):
            for c in range(block_col_start, block_col_end):
                if self._grid[r][c] == number:
                    return False
                
        return True

        