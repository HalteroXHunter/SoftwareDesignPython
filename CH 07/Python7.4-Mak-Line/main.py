from line import Line
from point import Point

def line_lengths():
    line_tuples = Line()
    p1 = (1, 1)
    p2 = (4, 5)
    print(f'  {p1 = }')
    print(f'  {p2 = }')
    print(f'{line_tuples.length(p1, p2) = }')
    print()
    
    line_dicts = Line()
    p1 = {'x': 1, 'y': 1}
    p2 = {'x': 4, 'y': 5}
    print(f'  {p1 = }')
    print(f'  {p2 = }')
    print(f'{line_dicts.length(p1, p2) = }')
    print()
    
    line_points = Line()
    p1 = Point(1, 1)
    p2 = Point(4, 5)
    print(f'  {p1 = }')
    print(f'  {p2 = }')
    print(f'{line_points.length(p1, p2) = }')
    print()
    
    line_ints = Line()
    print(f'{line_ints.length(1, 1, 4, 5) = }')
        
    line_floats = Line()
    print(f'{line_floats.length(1.0, 1.0, 4.0, 5.0) = }')

    line_list = Line()
    print(f'{line_list.length([1, 1, 4, 5]) = }')

    line_error = Line()
    print(f'{line_error.length(1, 1, 4) = }')

if __name__ == '__main__':
    try:
        line_lengths()
    except Exception as error:
        print()
        print(f'*** ERROR: {error}')
