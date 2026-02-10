from date import Date

if __name__ == '__main__':
    date = Date(2030, 1, 31)
    print(f'starting: {date = } {date.julian = }')
    
    date.month = 2
    print(f'modified: {date = } {date.julian = }')
    
    j = date.julian
    date.julian = j
    print(f'surprise: {date = } {date.julian = }')
