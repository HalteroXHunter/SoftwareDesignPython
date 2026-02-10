import sys
from sudoku import Sudoku

if __name__ == '__main__':
    file_name = sys.argv[1]
    sudoku = Sudoku(file_name)
    
    print('Input:')
    print()
    solved = sudoku.print_grid()
    
    solved = sudoku.solve()
    
    if solved:
        print()
        print('Solution:')
        print()
        sudoku.print_grid()
    else:
        print()
        print('No solution')
