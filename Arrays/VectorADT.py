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
        assert index < self.length() and index >= 0, "Invalid index"
        return self.theArray.elements[index]
    
    def __setItem__(self, index, value):
        assert index < self.length() and index >= 0, "Invalid index"
        self.theArray.elements[index] = value

    def append(self, item):
        if self.length() == self.theArray.__len__():
            cloneArray = list()
            for i in range(self.length()): cloneArray.append(self.__getItem__(i))
            newArray = Array(self.length() + 5)
            ndx = 0
            for i in cloneArray:
                newArray.setItem(ndx, i)
                ndx += 1
            newArray.setItem(ndx, item)
            self.theArray = newArray
        else: 
            ndx = self.length()
            self.theArray.setItem(ndx, item)


    def insert(self, index, item):
        pass

    def remove(self, index):
        assert index < self.length() and index >= 0 \
            and isinstance(index, int), "Invalid index"
        item = self.__getItem__(index)
        TargetIndex = index
        while self.theArray.elements[TargetIndex] is not None:
            self.__setItem__(TargetIndex, self.theArray.getItem(TargetIndex+1))
            TargetIndex += 1
        return item
    
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
    for i in range(10): V.append(i)
    V.remove(index=3)
    V.__setItem__(index=0, value=10)
    print(V.contains(0))
    print(V.length())
    print(V.snapshot())