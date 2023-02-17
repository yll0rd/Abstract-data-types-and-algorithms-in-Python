class Set:
    def __init__(self):
        self.Elements = list()

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
        else: return self.isSubsetOf(otherSet)

    def isSubsetOf(self, otherSet):
        for element in self:
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
    leo = Set()
    leo.add(1)
    leo.add(2)
    leo.add(3)
    print(leo.size())
    print(leo.Elements)