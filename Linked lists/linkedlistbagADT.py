class Bag:
    def __init__(self):
        self.head = None
        self.size = 0

    def len(self):
        return self.size
    
    def __contains__(self, target):
        curNode = self.head
        while curNode is not None and curNode.item != target:
            curNode = curNode.next
        return curNode is not None
        
    def add(self, item):
        newNode = BagListNode(item)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def remove(self, item):
        predNode = None
        curNode = self.head
        while curNode is not None and curNode.item != item:
            predNode = curNode
            curNode = curNode.next

        #The item has to be in the bag to remove it.
        assert curNode is not None, "The item must be in the bag."

        #Unlink the node and return the item.
        self.size -= 1
        if curNode is self.head:
            self.head = curNode.next
        else:
            predNode.next = curNode.next
        return curNode.item
    
    def removeAll(self):
        #Removing all the nodes in the linked list as from the head
        if self.head is not None: 
            self.size = 0
            curNode = self.head 
            while curNode.next is not None:
                curNode = curNode.next
                self.head = curNode.next        
                
    def __iter__(self):
        return BagIterator(self.head)
    
class BagListNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class BagIterator:
    def __init__(self, listHead):
        self.curNode = listHead

    def __iter__(self):
        return self
    
    def next(self):
        if self.curNode is None:
            raise StopIteration
        else:
            item = self.curNode.item
            self.curNode = self.curNode.next
            return item


if __name__ == "__main__":
    def iterate(B):
        ater = B.__iter__()
        while True:
            try:
                print(ater.next())
            except StopIteration:
                break

    Bag1 = Bag()
    Bag1.add(13)
    Bag1.add(15)
    Bag1.add("Go")
    print(Bag1.__contains__("Go"))
    print(f"The size of Bag1 is {Bag1.len()}")
    Bag1.remove(15)
    print(f"The size of Bag1 is {Bag1.len()}")
    print("The content in Bag1:")
    iterate(Bag1)
    print()
    Bag1.removeAll()
    print(f"The size of Bag1 is {Bag1.len()}")
    print("The content in Bag1:")
    iterate(Bag1)


    