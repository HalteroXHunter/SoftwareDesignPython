class Date:
    _MONTH_NAMES = (
        '',   
        'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
        'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'
    )
    
    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day
        
    def __str__(self):
        return (f'{Date._MONTH_NAMES[self._month]} '
                f'{self._day}, {self._year}')
