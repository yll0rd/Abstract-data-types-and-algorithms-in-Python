class Date:
    
    # Creates an object instance for the specified Gregorian date.
    def __init__(self,month,day,year):
        self.day = day
        self.month = month
        self.year = year
        self._julianDay = 0
        assert self._isValidGregorian( month, day, year ), "Invalid Gregorian date."
    # The first line of the equation, T = (M - 14) / 12, has to be changed
    # since Python's implementation of integer division is not the same
    # as the mathematical definition.
        tmp = 0
        if month < 3:
            tmp = -1
        self._julianDay = day - 32075 + (1461 * (year + 4800 + tmp) // 4) + (367 * (month - 2 - tmp * 12) // 12) - (3 * ((year + 4900 + tmp) // 100) // 4)

    # Extracts the appropriate Gregorian date component.
    def get_month( self ):
        return (self.toGregorian())[0] # returning M from (M, d, y)

    def get_day( self ):
        return (self.toGregorian())[1] # returning D from (m, D, y)

    def get_year( self ):
        return (self.toGregorian())[2] # returning Y from (m, d, Y)

    
    # Returns day of the week as an int between 0 (Mon) and 6 (Sun).
    def dayOfWeek( self ):
        mth, day, year = self.toGregorian()
        if mth < 3 :
            mth = mth + 12
            year = year - 1
        return ((13 * mth + 3) // 5 + day + year + year // 4 - year // 100 + year // 400) % 7

    # Returns the date as a string in Gregorian format.
    def __str__( self ):
        mth, day, year = self.toGregorian()
        return "%02d/%02d/%04d" % (mth, day, year)

    # Logically compares the two dates.
    def __eq__( self, otherDate ):
        return self._julianDay == otherDate._julianDay

    def __lt__( self, otherDate ):
        return self._julianDay < otherDate._julianDay

    def __le__( self, otherDate ):
        return self._julianDay <= otherDate._julianDay

    # The remaining methods are to be included at this point.
    def monthName(self):
        l = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        return l[self.month-1]

    def isLeapYear(self):
        yr = self.year
        if yr % 100 == 0:
            if yr % 400 == 0: return True
            else: return False
        elif yr % 4 == 0: return True
        else: return False

    def numDays(self, OtherDate):
        if self._julianDay > OtherDate._julianDay: return self._julianDay - OtherDate._julianDay
        else: return OtherDate._julianDay - self._julianDay

    def advanceBy(self, days):
        self._julianDay += days
        return self.__str__()

    def _isValidGregorian(self, mth, day, yr):
        if day not in range(1,32): return False
        if mth not in range(1,13): return False
        if yr < 0: return False
        return True

    # Returns the Gregorian date as a tuple: (mth, day, year).
    def toGregorian( self ):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        mth = 80 * A // 2447
        day = A - (2447 * mth // 80)
        A = mth // 11
        mth = mth + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return mth, day, year
