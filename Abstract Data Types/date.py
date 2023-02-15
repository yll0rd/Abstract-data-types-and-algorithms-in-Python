class Date:
    
    # Creates an object instance for the specified Gregorian date.
    def __init__(self,month,day,year):
        self.month = month
        self.day = day
        self.year = year
        self.julianDay = 0
        assert self._isValidGregorian( month, day, year ), "Invalid Gregorian date."
    # The first line of the equation, T = (M - 14) / 12, has to be changed
    # since Python's implementation of integer division is not the same
    # as the mathematical definition.
    tmp = 0
    if month < 3:
        tmp = -1
    julianDay = day - 32075 + (1461 * (year + 4800 + tmp) // 4) + (367 * (month - 2 - tmp * 12) // 12) - (3 * ((year + 4900 + tmp) // 100) // 4)

    # Extracts the appropriate Gregorian date component.
    def month( self ):
        return (self.toGregorian())[0] # returning M from (M, d, y)

    def day( self ):
        return (self.toGregorian())[1] # returning D from (m, D, y)

    def year( self ):
        return (self.toGregorian())[2] # returning Y from (m, d, Y)

    # Returns day of the week as an int between 0 (Mon) and 6 (Sun).
    def dayOfWeek( self ):
        month, day, year = self.toGregorian()
        if month < 3 :
            month = month + 12
            year = year - 1
        return ((13 * month + 3) // 5 + day + year + year // 4 - year // 100 + year // 400) % 7

    # Returns the date as a string in Gregorian format.
    def str( self ):
        month, day, year = self.toGregorian()
        return "%02d/%02d/%04d" % (month, day, year)

    # Logically compares the two dates.
    def __eq__( self, otherDate ):
        return self.julianDay == otherDate.julianDay

    def __lt__( self, otherDate ):
        return self.julianDay < otherDate.julianDay

    def __le__( self, otherDate ):
        return self.julianDay <= otherDate.julianDay

    # The remaining methods are to be included at this point.
    # ......

    # Returns the Gregorian date as a tuple: (month, day, year).
    def toGregorian( self ):
        A = self.julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return month, day, year
