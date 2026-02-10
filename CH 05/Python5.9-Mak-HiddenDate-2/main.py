from date import Date
from employee import Employee

if __name__ == '__main__':
    marys_birthdate = Date(2000, 1, 10)
    mary = Employee(1234567890, 'Mary', marys_birthdate)
    print(mary)
    
    marys_birthdate.julian += 366
    print(mary)
    
    date = mary.birthdate
    date.julian += 365
    print(mary)