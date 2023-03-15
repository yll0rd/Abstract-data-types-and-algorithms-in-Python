def bubbleSort(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if theSeq[j] > theSeq[j + 1]:
                theSeq[j], theSeq[j + 1] = theSeq[j + 1], theSeq[j]
    return theSeq


theList1 = [2, 4, 1, 0, 5, 3]
theList2 = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
print(bubbleSort(theList1))
print(bubbleSort(theList2))
