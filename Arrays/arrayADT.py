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
        assert index >= 0 and index < self.__len__(), "Array subscript out of range"
        return self.elements[index]
    
    def setItem(self, index, value):
        assert index >= 0 and index < self.__len__(), "Array subscript out of range"
        self.elements[index] = value

    def clear(self, value):
        for i in range(self.size):
            self.elements[i] = value

    def __iter__(self):
        return ArrayIterator(self.elements)

class ArrayIterator:
    def __init__(self, theArray):
        self.arr = theArray
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.arr):
            entry = self.arr[self.index]
            self.index += 1
            return entry
        else:
            raise StopIteration
    
