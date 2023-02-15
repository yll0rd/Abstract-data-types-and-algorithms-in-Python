from date import Date


def main():
    bornBefore = Date(2006,1,14)
    print(bornBefore)
    date = promptandExactDate()
    print()
    while date != None:
        if date <= bornBefore:
            print("Is at least 17 of age: ", date)
        date = promptandExactDate()

def promptandExactDate():
    print("Enter a birth date.")
    month = int(input("month (0 to quit): "))
    if month == 0 :
        return None
    else :
        day = int( input("day: ") )
        year = int( input("year: ") )
        return Date(year,month,day)

main()