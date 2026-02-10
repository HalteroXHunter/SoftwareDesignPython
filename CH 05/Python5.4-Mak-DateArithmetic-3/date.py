import math

class Date:
    _JANUARY  = 1
    _FEBRUARY = 2
    _DECEMBER = 12

    _GREGORIAN_START_YEAR = 1582
    _GREGORIAN_START_MONTH = 10
    _GREGORIAN_START_DATE = 15
    _JULIAN_END_DATE = 4
    
    _MAX_DAYS_IN_MONTH = 31
    _MONTHS_PER_YEAR   = 12
    
    _DAYS_IN_MONTH = ( 31, 28, 31, 30, 31, 30, 
                       31, 31, 30, 31, 30, 31 )

    @staticmethod
    def _to_julian(year, month, day):

        y = year
        if year < 0: y += 1
        
        m = month
        if month > Date._FEBRUARY: m += 1
        else:
            y -= 1
            m += 13
            
        j = (math.floor(math.floor(365.25*y) + math.floor(30.6001*m))
                    + day + 1720995)

        term = (Date._MAX_DAYS_IN_MONTH
                    *(month + Date._MONTHS_PER_YEAR*year))
        
        GREGORIAN_CUTOFF = (
            Date._GREGORIAN_START_DATE +
            Date._MAX_DAYS_IN_MONTH
                *(Date._GREGORIAN_START_MONTH +
                  Date._MONTHS_PER_YEAR*Date._GREGORIAN_START_YEAR)
            )
        
        if day + term >= GREGORIAN_CUTOFF:
            x = math.floor(0.01*y)
            j += 2 - x + math.floor(0.25*x)
        
        return j
    
    @staticmethod
    def _to_ymd(julian):
        GREGORIAN_CUTOFF = 2299161
        
        ja = julian
        
        if julian >= GREGORIAN_CUTOFF:
            jalpha = math.floor(
                (float(julian - 1867216) - 0.25)/36524.25)
            ja += 1 + jalpha - math.floor(0.25*jalpha)
            
        jb = ja + 1524
        jc = math.floor(
                6680.0 + (float(jb - 2439870) - 122.1)/365.25)
        jd = math.floor(365*jc + (0.25*jc))
        je = math.floor((jb - jd)/30.6001)
        
        day = jb - jd - math.floor(30.6001*je)
        
        month = je - 1
        if month > Date._DECEMBER: month -= 12
        
        year = jc - 4715
        if month > Date._FEBRUARY: year -= 1
        if year <= 0: year -= 1
        
        return (year, month, day)

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
    
    def __init__(self, *parms):
        if len(parms) == 1:
            self._julian = parms[0]
            self._ymd_valid = False
            self._julian_valid = True
        else:
            self._year, self._month, self._day = parms
            self._ymd_valid = True
            self._julian_valid = False
    
    def _validate_ymd(self):
        if not self._ymd_valid:
            self._year, self._month, self._day = \
                                    Date._to_ymd(self._julian)
            self._ymd_valid = True
            
    def _validate_julian(self):
        if not self._julian_valid:
            self._julian = \
                Date._to_julian(self._year, self._month, self._day)
            self._julian_valid = True
        
    @property
    def year(self):
        self._validate_ymd()
        return self._year
        
    @property
    def month(self):
        self._validate_ymd()
        return self._month
        
    @property
    def day(self):
        self._validate_ymd()
        return self._day
    
    def add_days(self, n): 
        self._validate_julian()
        return Date(self._julian + n)
    
    def days_from(self, other): 
        self._validate_julian()
        other._validate_julian()
        return self._julian - other._julian
    
    def __repr__(self):
        date_string = f'{self.month}/{self.day}/'
        if self.year > 0: date_string += str(self.year)
        else:             date_string += str(-self.year) + ' BCE'
        
        return date_string
    