from date import Date

if __name__ == '__main__':
    date1 = Date(2025, 9, 2)
    date2 = Date(2027, 4, 3)

    print(f'{date1 = }')   
    print(f'{date2 = }')
    
    print()
    
    count = date2.days_from(date1)
    print(f'{count = }')
    
    print(f'{date1.add_days(count) = }')    
    print(f'      should be {date2 = }')
    
    print()
    
    count = date1.days_from(date2)
    print(f'{count = }')
    
    print(f'{date2.add_days(count) = }')    
    print(f'      should be {date1 = }')
