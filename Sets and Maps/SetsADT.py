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

if __name__ == '__main__':
    leo = Set()
    leo.add(1)
    leo.add(2)
    leo.add(3)
    print(leo.size())
    print(leo.Elements)