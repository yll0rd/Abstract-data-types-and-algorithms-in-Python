from date import Date


def main():
    bornBefore = Date(1,14,2023)
    print(bornBefore)
    print(bornBefore.monthName())
    print(bornBefore.dateOfWeekName())
    print(bornBefore.dateOfYear())
    # print(bornBefore.isLeapYear())
    # print(bornBefore.numDays(Date(1,20,2006)))
    # print(bornBefore.advanceBy(65))
    # date = PromptAndExactDate()
    # print()
    # while date is not None:
    #     if date <= bornBefore:
    #         print("Is at least 17 of age: ", date)
    #     date = PromptAndExactDate()

def PromptAndExactDate():
    print("Enter a birth date.")
    month = int(input("month (0 to quit): "))
    if month == 0 :
        return None
    else :
        day = int( input("day: ") )
        year = int( input("year: ") )
        return Date(month,day,year)

main()