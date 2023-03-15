# Implementation of the linear search on an unsorted sequence.
def linearSearch(theValues, target):
    assert isinstance(theValues, (list, str)), "First parameter entered must be iterable."
    n = len(theValues)
    for i in range(n):
        # If the target is in the ith element, return True
        if theValues[i] == target:
            return True
    return False  # If not found, return False


aString = "235"
aList = [i for i in range(10)]

print(aString)
print(aList)
print(linearSearch(aString, 2))
print(linearSearch(aString, "2"))
print(linearSearch(aList, 3))
print(linearSearch(aList, 10))


# Implementation of the linear search on a sorted sequence.
def sortedLinearSearch(theValues, item):
    assert isinstance(theValues, list), "First parameter entered must a list."
    n = len(theValues)
    for i in range(n):
        if theValues[i] == item:
            return True
        elif theValues[i] > item:
            break
    return False


L = [num for num in range(0, 10, 2)]
print(L)
print(sortedLinearSearch(L, 7))
print(sortedLinearSearch(L, 6))


# Searching for the smallest value in an unsorted sequence.
def findSmallest(theValues):
    n = len(theValues)
    smallest = theValues[0]
    for i in range(1, n):
        if theValues[i] < smallest:
            smallest = theValues[i]
    return smallest


l1 = [8, 3, 6, 9, 1, 10]
print(findSmallest(l1))
