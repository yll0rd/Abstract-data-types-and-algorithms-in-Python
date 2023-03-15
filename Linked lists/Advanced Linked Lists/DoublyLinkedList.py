# The list is sorted
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.probe = None
        self.size = 0

    def len(self):
        return self.size

    def isEmpty(self):
        return self.head is None

    def insert(self, value):
        newNode = DListNode(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = self.head
        else:
            if value < self.head.data:  # insert before head
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif value > self.tail.data:  # insert after tail
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
            else:
                curNode = self.head
                while curNode is not None and curNode.data <= value:
                    curNode = curNode.next
                newNode.next = curNode
                newNode.prev = curNode.prev
                curNode.prev.next = newNode
                curNode.prev = newNode
        self.size += 1

    def remove(self, value):
        assert not self.isEmpty(), f"Can't remove '{value}' from an empty list"
        assert self.contains(value), f"'{value}' is not in the list"
        if value == self.head.data:
            self.head = self.head.next
        elif value == self.tail.data:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            curNode = self.head
            while curNode is not None and curNode.data != value:
                if curNode.data >= value: break
                curNode = curNode.next
            curNode.prev.next = curNode.next
            curNode.next.prev = curNode.prev
        self.size -= 1

    def revTraversal(self):
        curNode = self.tail
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.prev

    def contains(self, target):
        # Make sure the list is not empty
        if self.head is None:
            return False
        # If there's no initial probe, initialize it
        # to the first node
        elif self.probe is None:
            self.probe = self.head

        # If the target comes before the probe node, we traverse backward;
        # otherwise traverse forward.
        if target < self.probe.data:
            while self.probe is not None and target <= self.probe.data:
                if target == self.probe.data:
                    return True
                else:
                    self.probe = self.probe.prev
        else:
            while self.probe is not None and target >= self.probe.data:
                if target == self.probe.data:
                    return True
                else:
                    self.probe = self.probe.next
        # If the target is not found in the list, return False.
        return False

    def snapshot(self):
        curNode = self.head
        listNode = list()
        while curNode is not None:
            listNode.append(curNode.data)
            curNode = curNode.next
        print(listNode)


class DListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

from random import randint

if __name__ == '__main__':
    D = DoubleLinkedList()
    for i in range(5):
        D.insert(i)
    print(D.len())
    D.snapshot()
    while True:
        i = randint(0,5)
        if D.contains(i):
            D.remove(i)
            break
    print(D.len())
    D.snapshot()
