class PriorityQueue:
    def __init__(self):
        self.qhead = None
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
            if priority < self.qhead.priority:
                entry.next = self.qhead
                self.qhead = entry
            else:
                CurNode = self.qhead
                while CurNode.next is not None:
                    if entry.priority < CurNode.next.priority: break
                    CurNode = CurNode.next
                entry.next = CurNode.next
                CurNode.next = entry
        self.qsize += 1

    def dequeue(self):
        assert not self.isEmpty(), "Queue is empty"
        item = self.qhead.item
        self.qhead = self.qhead.next
        self.qsize -= 1
        return item

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

