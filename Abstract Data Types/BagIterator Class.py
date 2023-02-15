
class BagIterator():
    def __init__(self, theList):
        self.BagItems = theList
        self.curItem = 0

    def iter(self): #To convert the list to an iterator object
        return self

    def next(self): #To return the next item in the container
        if self.curItem < len(self.BagItems):
            item = self.BagItems[self.curItem]
            self.curItem += 1
            return item
        else:
            raise StopIteration


if __name__ == "__main__":
    l = [1,2,3,"Okayy"]
    # print(type(l))
    it = BagIterator(l)
    # print(type(it))
    while True:
        try:
            item = it.next()
            print(item)
        except StopIteration:
            break
