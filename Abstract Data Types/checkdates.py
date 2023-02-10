from datetime import date

def main():
    bornBefore = date(2006,1,14)
    print(bornBefore)
    Date = promptandExactDate()
    print()
    while Date != None:
        if Date <= bornBefore:
            print("Is at least 17 of age: ", Date)
        Date = promptandExactDate()

def promptandExactDate():
    print("Enter a birth date.")
    month = int(input("month (0 to quit): "))
    if month == 0 :
        return None
    else :
        day = int( input("day: ") )
        year = int( input("year: ") )
        return date(year,month,day)

main()