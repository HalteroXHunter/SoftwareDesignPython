from date import Date

if __name__ == '__main__':
    date1 = Date(2025, 9, 2)
    date2 = Date(2027, 4, 3)

    print(f'{date1 = }')   
    print(f'{date2 = }')    
    print()
    
    print(f'{date1 = } Julian number {date1.julian = :,d}')

    date2.julian = date1.julian
    print(f'{date2 = } Julian number {date2.julian = :,d}')
    print()
    
    for j in [0, 2440000, 3000000]:
        date1.julian = j
        print(f'set Julian number {j = :9,d} ==> {date1 = }')