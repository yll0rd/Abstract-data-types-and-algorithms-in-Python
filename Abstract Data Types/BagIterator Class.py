
class BagIterator():
    def __init__(self, theList):
        self.BagItems = theList
        self.curItem = 0

    def __iter__(self): #To convert the list to an iterator object
        return self

    def __next__(self): #To return the next item in the container
        if self.curItem < len(self.BagItems):
            item = self.BagItems[self.curItem]
            self.curItem += 1
            return item
        else:
            raise StopIteration

l = [1,2,3,"Okayy"]
# print(type(l))
it = l.__iter__()
# print(type(it))
while True:
    try:
        item = it.__next__()
        print(item)
    except StopIteration:
        break
