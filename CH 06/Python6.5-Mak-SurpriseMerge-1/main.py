from sortedlist import SortedList
from collections import Counter

if __name__ == '__main__':
    list1 = [ 2, 5, 5, 5, 7, 11, 11, 11, 13, 13 ]
    list2 = [ 0, 1, 2, 2, 2, 2, 4, 4, 5, 6, 7, 7, 9, 11 ]
    
    print(f'      {list1 = }')
    print(f'      {list2 = }')
    
    merged_list = SortedList.merge(list1, list2)
    print(f'{merged_list = }')
    
    print()
    print('Frequency table')
    
    for i, count in Counter(merged_list).items():
        print(f'{i:7d}: {count}')
