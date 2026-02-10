class Date:
    _JANUARY  = 1
    _FEBRUARY = 2
    _DECEMBER = 12

    _GREGORIAN_START_YEAR = 1582
    _GREGORIAN_START_MONTH = 10
    _GREGORIAN_START_DATE = 15
    _JULIAN_END_DATE = 4
    
    _DAYS_IN_MONTH = ( 31, 28, 31, 30, 31, 30, 
                       31, 31, 30, 31, 30, 31 )
    
    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day
        
    @property
    def year(self): return self._year
    
    @property
    def month(self): return self._month
    
    @property
    def day(self): return self._day
    
    def __repr__(self):
        date_string = f'{self.month}/{self.day}/'
        if self.year > 0: date_string += str(self.year)
        else:             date_string += str(-self.year) + ' BCE'
        
        return date_string
    
    @staticmethod
    def _days_in_month(year, month):
        if (month == Date._FEBRUARY) and Date._is_leap_year(year): 
            return 29
        else: 
            return Date._DAYS_IN_MONTH[month - 1]
    
    @staticmethod
    def _is_leap_year(year):
        if year%4 != 0: return False
        if year < Date._GREGORIAN_START_YEAR: return True
        
        return (year%100 != 0) or (year%400 == 0)
        
    def _compare_to(self, other):
        if self._year > other.year: return 1
        if self._year < other.year: return -1
        
        if self._month > other.month: return 1
        if self._month < other.month: return -1
        
        return self._day - other.day
    
    def _next_date(self):
        y = self._year
        m = self._month
        d = self._day
        
        if (    (y == Date._GREGORIAN_START_YEAR)
            and (m == Date._GREGORIAN_START_MONTH)
            and (d == Date._JULIAN_END_DATE)
        ): d = Date._GREGORIAN_START_DATE
        elif d < Date._days_in_month(y, m): d += 1
        else:
            d = 1
            m += 1
            
            if m > Date._DECEMBER:
                m = Date._JANUARY
                y += 1
                
                if y == 0: y += 1
        
        return Date(y, m, d)
    
    def _previous_date(self):
        y = self._year
        m = self._month
        d = self._day
        
        if (    (y == Date._GREGORIAN_START_YEAR)
            and (m == Date._GREGORIAN_START_MONTH)
            and (d == Date._GREGORIAN_START_DATE)
        ): d = Date._JULIAN_END_DATE
        elif d > 1: d -= 1
        else:
            m -= 1
            
            if m < Date._JANUARY:
                m = Date._DECEMBER
                y -= 1
                
                if y == 0: y -= 1
                
            d = Date._days_in_month(y, m)
            
        return Date(y, m, d)
    
    def add_days(self, n):
        date = self
        
        while n > 0:
            date = date._next_date()
            n -= 1
            
        while n < 0:
            date = date._previous_date()
            n += 1
            
        return date
    
    def days_from(self, other):
        date = self
        
        n = 0
        
        while date._compare_to(other) > 0:
            date = date._previous_date()
            n += 1
            
        while date._compare_to(other) < 0:
            date = date._next_date()
            n -= 1
            
        return n
    