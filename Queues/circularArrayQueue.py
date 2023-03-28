from Arrays.arrayADT import Array


class Queue:
    # Creates an empty queue
    def __init__(self, maxSize):
        self.count = 0
        self.front = 0
        self.ndxBack = maxSize - 1
        self.qArray = Array(maxSize)

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.qArray.__len__()

    def __len__(self):
        return self.count

    def enqueue(self, item):
        assert not self.isFull(), "Cannot enqueue to full queue."
        maxQ = len(self.qArray)
        self.ndxBack = (self.ndxBack + 1) % maxQ
        self.qArray[self.ndxBack] = item
        self.count += 1

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        item = self.qArray[self.front]
        maxQ = len(self.qArray)
        self.front = (self.front + 1) % maxQ
        self.count -= 1
        return item
