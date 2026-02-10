class Date:
    _MONTH_NAMES = [
        'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
        'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'
    ]
    
    def __init__(self, y, m, d):
        self._year = y
        self._month = m
        self._day = d
            
    def __str__(self):
        return (f'{Date._MONTH_NAMES[self._month]} '
                f'{self._day}, {self._year}')
