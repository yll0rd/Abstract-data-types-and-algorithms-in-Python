def selectionSort(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
        SmallNdx = i
        for j in range(i + 1, n):
            if theSeq[j] < theSeq[SmallNdx]:
                SmallNdx = j

        if SmallNdx != i:
            theSeq[i], theSeq[SmallNdx] = theSeq[SmallNdx], theSeq[i]
        print(theSeq)


theList = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
selectionSort(theList)
print(theList)
