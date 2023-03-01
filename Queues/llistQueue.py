class Queue:
    # Creates an empty queue
    def __init__(self):
        self.qhead = None
        self.qtail = None
        self.qsize = 0

    def isEmpty(self):
        return self.qhead is None
    
    def size(self):
        return self.qsize
    
    def enqueue(self, item):
        node = QueueNode(item)
        if self.isEmpty():
            self.qhead = node
        else:
            self.qtail.next = node
        self.qsize += 1
        self.qtail = node

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        node = self.qhead
        # If there's only one element in the queue,
        # then, there's no tail node
        if self.qhead is self.qtail:
            self.qtail = None
        self.qhead = self.qhead.next
        self.qsize -= 1
        return node.item



class QueueNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None