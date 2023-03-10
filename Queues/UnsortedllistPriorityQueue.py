class PriorityQueue:
    def __init__(self):
        self.qhead = None
        self.qtail = None
        self.qsize = 0

    def isEmpty(self):
        return self.qhead is None

    def size(self):
        return self.qsize

    def enqueue(self, item, priority):
        entry = PriorityQEntry(item, priority)
        if self.isEmpty():
            self.qhead = entry
        else:
            self.qtail.next = entry
        self.qsize += 1
        self.qtail = entry

    def dequeue(self):
        assert not self.isEmpty(), "Queue is empty"
        self.qsize -= 1
        # Traversing through Queue until it
        # finds the smallest priority node
        lowest = self.qhead.priority
        Cur = self.qhead.next
        while Cur is not None:
            if lowest > Cur.priority:
                lowest = Cur.priority
            Cur = Cur.next

        # Unlink the node and return the item.
        PrevNode = None
        CurNode = self.qhead
        while CurNode is not None:
            if CurNode.priority == lowest:
                if CurNode is self.qhead:
                    item = self.qhead.item
                    self.qhead = self.qhead.next
                    return item
                else:
                    item = CurNode.item
                    PrevNode.next = CurNode.next
                    return item
            PrevNode = CurNode
            CurNode = CurNode.next



class PriorityQEntry(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.next = None


if __name__ == '__main__':
    Q = PriorityQueue()
    Q.enqueue("purple", 5)
    Q.enqueue("black", 1)
    Q.enqueue("orange", 3)
    Q.enqueue("white", 0)
    Q.enqueue("green", 1)
    Q.enqueue("yellow", 5)

    for i in range(Q.size()):
        print(Q.dequeue())

