class Map:
    def __init__(self):
        self.entryList = list() 

    def size(self):
        return len(self.entryList)
    
    def __contains__(self,key):
        ndx = self.findPosition(key)
        return ndx is not None
    
    """Adds a new entry to the map if the key does exist. Otherwise, the
    new value replaces the current value associated with the key."""
    def add(self, key, value):
        ndx = self.findPosition(key)
        if ndx is not None:
            self.entryList[ndx].value = value
            return False
        else:
            entry = _MapEntry(key, value)
            self.entryList.append(entry)
            return True
        
    def valueOf(self, key):
        ndx = self.findPosition(key)
        assert ndx is not None, "Invalid map key"
        return self.entryList[ndx].value
    
    def remove(self, key):
        ndx = self.findPosition(key)
        assert ndx is not None, "Invalid map key"
        self.entryList.pop(ndx)

    # def __iter__(self):
    #     return _MapInterator(self.entryList)

    """Helper method used to find the index position of a category. If the
    key is not found, None is returned."""
    def findPosition(self, key):
        for i in range(len(self.entryList)):
            if self.entryList[i].key == key:
                return i
        return None

# Storage class for holding the key/value pairs.
class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


if __name__ == "__main__":
    m = Map()
    m.add(1, "Leo")
    m.add(2, "Grant")
    m.add(1, "Brice")
    m.remove(2)
    for i in m.entryList:
        print(i.key, end=": ")
        print(m.valueOf(i.key))