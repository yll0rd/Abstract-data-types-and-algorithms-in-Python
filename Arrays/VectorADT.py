from arrayADT import Array

class Vector:
    def __init__(self):
        self.theArray = Array(2)
        self.theArray.clear(None)

    def length(self):
        len = 0
        item = self.theArray.getItem(len)
        while item is not None:
            len += 1
            if len >= self.theArray.__len__(): break
            item = self.theArray.getItem(len)
        return len
    
    def contains(self, item):
        target, i  = 0, 0
        while target is not None and i < self.theArray.__len__():
            target = self.theArray.getItem(i)
            if item == target: return True
            i += 1
        return False
    
    def __getItem__(self, index):
        assert index in range(self.length()), "Index out of range"
        assert isinstance(index, int), "Invalid index"
        return self.theArray.elements[index]
    
    def __setItem__(self, index, value):
        assert index in range(self.length()), "Index out of range"
        assert isinstance(index, int), "Invalid index"
        self.theArray.elements[index] = value

    def append(self, item):
        if self.length() == self.theArray.__len__():
            cloneArray = list()
            for i in range(self.length()): cloneArray.append(self.__getItem__(i))
            cloneArray.append(item)
            newArray = Array(self.length() + 3)
            ndx = 0
            for i in cloneArray:
                newArray.setItem(ndx, i)
                ndx += 1
            self.theArray = newArray
        else: 
            ndx = self.length()
            self.theArray.setItem(ndx, item)


    def insert(self, index, item):
        assert index in range(self.length()), "Index out of range"
        assert isinstance(index, int), "Invalid index"
        if self.length() == self.theArray.__len__():
            cloneArray = list()
            for i in range(self.length()): cloneArray.append(self.__getItem__(i))
            cloneArray.insert(index,item)
            newArray = Array(self.length() + 2)
            ndx = 0
            for i in cloneArray:
                newArray.setItem(ndx, i)
                ndx += 1
            self.theArray = newArray
        else: 
            for i in range(self.length(), -1, -1):
                if i == index: break
                self.theArray.setItem(i, self.__getItem__(i-1))
            self.theArray.setItem(index, item)

    def remove(self, index):
        assert index in range(self.length()), "Index out of range"
        assert isinstance(index, int), "Invalid index"
        item = self.__getItem__(index)
        ndx = index
        while self.theArray.elements[ndx] is not None:
            self.__setItem__(ndx, self.theArray.getItem(ndx+1))
            ndx += 1
        return item
    
    def extend(self, otherVector):
        assert isinstance(otherVector, Vector), "Invalid otherVector"
        LenArray = self.theArray.__len__() + otherVector.theArray.__len__()
        LenVector = self.length() + otherVector.length()
        NewArray = Array(LenArray)
        for i in range(self.length()):
            NewArray.setItem(i, self.__getItem__(i))
        ndx = 0
        for i in range(self.length(), LenVector) :
            NewArray.setItem(i, otherVector.__getItem__(ndx))
            ndx += 1
        self.theArray = NewArray

    def subVector(self, start, end):
        assert start in range(self.length()) and \
            end in range(self.length()), "Indices out of range"
        assert isinstance(start, int) and isinstance(end, int), "Invalid index"
        newArray = Array(self.length())
        ndx = 0
        for i in range(start, end+1):
            newArray.setItem(ndx, self.__getItem__(i))
            ndx += 1
        return newArray.snapshot()

    def indexOf(self, item):
        assert self.contains(item), f"{item} not in the vector"
        for TargetIndex in range(self.length()):
            if item == self.__getItem__(TargetIndex):
                return TargetIndex
    
    def __iter__(self):
        return VectorIterator(self) 

    def snapshot(self):
        snap = list()
        It = self.__iter__()
        for i in range(self.length()):
            try:
                snap.append(It.next())
            except StopIteration:
                break
        return snap

class VectorIterator(object):
    def __init__(self, vector):
        self.vector = vector
        self.curNdx = 0
    
    def iter(self):
        return self

    def next(self):
        if self.curNdx < self.vector.length():
            item = self.vector.__getItem__(self.curNdx)
            self.curNdx += 1
            return item
        else: raise StopIteration 




if __name__ == "__main__":
    V = Vector()
    V1 = Vector()
    for i in range(10,0,-1): V.append(i)
    for i in range(10,20): V1.append(i)

    print("V:", V.snapshot())
    print("The length of V is:", V.length())
    V.extend(V1)
    print("The index of 1 in V is:", V.indexOf(1))
    print("Does V contain 0?", V.contains(0))
    print()
    print("V1:", V1.snapshot())
    print("Extended V:", V.snapshot())
    print("The length of extended V is:", V.length())
    print()
    print("The subVector of the extended V from index 1 to 12:\n", V.subVector(1,12))
