class Set:
    def __init__(self, initElements = None):
        self.Elements = list()
        if initElements is not None:
            self.Elements = list(initElements)

    def size(self):
        return len(self.Elements)

    def __contains__(self, element):
        return element in self.Elements

    def add(self, element):
        if element not in self:
            self.Elements.append(element)

    def remove(self, element):
        assert element in self, "The element must be in the set"
        self.Elements.remove(element)

    def equal(self, otherSet):
        if len(otherSet.Elements) != len(self.Elements): return False
        for element in otherSet.Elements:
            if not self.__contains__(element): return False
        return True

    def isSubsetOf(self, otherSet):
        if self.equal(otherSet): return False
        for element in self.Elements:
            if element not in otherSet: return False
        return True

    def union(self, otherSet):
        newSet = Set()
        newSet.Elements.extend(self.Elements)
        for element in otherSet:
            if element not in self:
                newSet.add(element)
        return newSet

    def intersect(self, otherSet):
        newSet = Set()
        for element in self:
            if element in otherSet:
                newSet.add(element)
        return newSet

    def difference(self, otherSet):
        newSet = Set()
        newSet.Elements.extend(self.Elements)
        for element in otherSet:
            if element in self:
                newSet.remove(element)

if __name__ == '__main__':
    leo = Set([1,3,4])
    brice = Set()
    brice.add(1)
    brice.add(2)
    brice.add(3)
    brice.remove(2)
    print(leo.size())
    print(leo.Elements)
    print(brice.Elements)
    print(brice.isSubsetOf(leo))
    print(leo.isSubsetOf(leo))