import ctypes


class Array:
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self.size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self.elements = PyArrayType()
        # Initialize each element
        self.clear(None)

    def __len__(self):
        return self.size

    def getItem(self, index):
        assert 0 <= index < self.__len__(), "Array subscript out of range"
        return self.elements[index]

    def setItem(self, index, value):
        assert 0 <= index < self.__len__(), "Array subscript out of range"
        self.elements[index] = value

    def clear(self, value):
        for i in range(self.size):
            self.elements[i] = value

    def snapshot(self):
        snap = list()
        It = self.__iter__()
        for i in range(self.size):
            try:
                snap.append(It.__next__())
            except StopIteration:
                break
        return snap

    def __iter__(self):
        return ArrayIterator(self.elements)


class ArrayIterator:
    def __init__(self, theArray):
        self.arr = theArray
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.arr) and self.arr[self.index] is not None:
            entry = self.arr[self.index]
            self.index += 1
            return entry
        else:
            raise StopIteration


# Implementation of the Array2D ADT using an array of arrays
class Array2D:
    def __init__(self, numRows, numCols):
        # Create a 1-D array to store an array reference for each row.
        self.theRows = Array(numRows)
        # Create the 1-D arrays for each row of the 2-D array.
        for i in range(numRows):
            self.theRows.setItem(i, Array(numCols))

    def getnumRows(self):
        return self.theRows.__len__()

    def isEmpty(self):
        for row in range(self.getnumRows()):
            theArray = self.theRows.getItem(row)
            for col in range(self.getnumCols()):
                if theArray.getItem(col) is not None:
                    return False
        return True

    def getnumCols(self):
        n = self.theRows.getItem(0)
        return n.__len__()

    def clear(self, value):
        for row in range(self.getnumRows()):
            theArray = self.theRows.getItem(row)
            for col in range(self.getnumCols()):
                theArray.setItem(col, value)

    def __getItem__(self, indexTuple):
        assert len(indexTuple) == 2, "Invalid number of array subscripts."
        row = indexTuple[0]
        col = indexTuple[1]
        assert 0 <= row < self.getnumRows() \
               and 0 <= col < self.getnumCols(), \
            "Array subscript out of range."
        theArray = self.theRows.getItem(row)
        return theArray.getItem(col)

    def __setItem__(self, indexTuple, value):
        assert len(indexTuple) == 2, "Invalid number of array subscripts."
        row = indexTuple[0]
        col = indexTuple[1]
        assert 0 <= row < self.getnumRows() \
               and 0 <= col < self.getnumCols(), \
            "Array subscript out of range."
        theArray = self.theRows.getItem(row)
        theArray.setItem(col, value)


if __name__ == "__main__":
    a = Array2D(2, 3)
    a.clear(None)
    if not a.isEmpty():
        for row in range(a.getnumRows()):
            for col in range(a.getnumCols()):
                val = eval(input(f"Enter a[{row}][{col}]: "))
                a.__setItem__((row, col), val)

    for row in range(a.getnumRows()):
        for col in range(a.getnumCols()):
            print(f"A[{row}][{col}]: {a.__getItem__((row, col))}")
