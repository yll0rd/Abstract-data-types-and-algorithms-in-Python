class PriorityQueue:
    def __init__(self):
        self.qList = list()
        
    def isEmpty(self):
        return len(self.qList) == 0

    def size(self):
        return len(self.qList)

    def enqueue(self, item, priority):
        entry = PriorityQEntry(item, priority)
        index = 0
        i = 0
        while index < len(self.qList) and entry.priority >= self.qList[i].priority:
            index = index + 1
            i += 1
        self.qList.insert(index, entry)

    def dequeue(self):
        assert not self.isEmpty(), "Queue is empty"
        return self.qList.pop(0).item


class PriorityQEntry(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority


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
