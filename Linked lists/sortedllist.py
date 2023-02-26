class Sortedllist():
    def __init__(self):
        self.head = None

    def insert(self, value):
        # Find the insertion point for the new value.
        predNone = None
        curNode = self.head
        while curNode is not None and value > curNode.data:
            predNone = curNode
            curNode = curNode.next
        # Creating the new node
        newNode = BagListNode(value)
        newNode.next = curNode
        # Linking the new node into the list
        if curNode is self.head:
            self.head = newNode
        else:
            predNone.next = newNode

    def delete(self, item):
        predNode = None
        curNode = self.head
        while curNode is not None and curNode.data != item:
            predNode = curNode
            curNode = curNode.next
        
        #The item has to be in the bag to remove it.
        assert curNode is not None, "The item must be in the bag."

        #Unlink the node and return the item.
        if curNode is self.head:
            self.head = curNode.next
        else:
            predNode.next = curNode.next

    def sortedsearch(self, target):
        curNode = self.head
        while curNode is not None and curNode.data <= target:
            if curNode.data == target:
                return True
            else:
                curNode = curNode.next
        return False
    
    def __iter__(self):
        return sortllistIterator(self.head)

class BagListNode(object):
    def __init__(self, item):
        self.data = item
        self.next = None

class sortllistIterator:
    def __init__(self, listHead):
        self.curNode = listHead

    def __iter__(self):
        return self
    
    def next(self):
        if self.curNode is None:
            raise StopIteration
        else:
            item = self.curNode.data
            self.curNode = self.curNode.next
            return item


if __name__ == '__main__':
    def iterate(B):
        ater = B.__iter__()
        while True:
            try:
                print(ater.next(), end=" ")
            except StopIteration:
                break

    Bag1 = Sortedllist()
    Bag1.insert(7)
    Bag1.insert(6)
    Bag1.insert(8)
    Bag1.insert(1)
    Bag1.insert(2)
    Bag1.delete(7)
    print("The content in Bag1:")
    iterate(Bag1)
    print()
    print(Bag1.sortedsearch(1))
    print(Bag1.sortedsearch(7))