# The list is sorted
class CircularLinkedList:
    def __init__(self):
        self.listRef = None
        self.size = 0

    def len(self):
        return self.size

    def isEmpty(self):
        return self.listRef is None

    def insert(self, item):
        newNode = CircularLinkedListNode(item)
        if self.isEmpty():
            self.listRef = newNode
            newNode.next = newNode
        else:
            if value < self.listRef.item:  # insert in front
                newNode.next = self.listRef.next
                self.listRef.next = newNode
            elif value > self.listRef.item:  # insert in back
                self.listRef.next = newNode
                newNode.next = self.listRef.next
                self.listRef = newNode
            else:
                predNode = None
                curNode = self.listRef
                while curNode is not None and curNode.data <= item:
                    predNode = curNode
                    curNode = curNode.next
                predNode.next = newNode
                newNode.next = curNode
        self.size += 1

    def remove(self, item):
        predNode = None
        curNode = self.head
        while curNode is not None and curNode.item != item:
            predNode = curNode
            curNode = curNode.next

        # The item has to be in the bag to remove it.
        assert curNode is not None, "The item must be in the bag."

        # Unlink the node and return the item.
        self.size -= 1
        if curNode is self.head:
            self.head = curNode.next
        else:
            predNode.next = curNode.next
        return curNode.item

    def traverse(self):
        curNode = self.listRef
        done = self.listRef is None
        while not done:
            curNode = curNode.next
            print(curNode.item)
            done = curNode.item == listRef


class CircularLinkedListNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None
