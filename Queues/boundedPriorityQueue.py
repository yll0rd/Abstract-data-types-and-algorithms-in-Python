# Implementation of the bounded Priority Queue ADT using an array of
# queues in which the queues are implemented using a linked list.
from CircularArrayQueue.arrayADT import Array
from llistQueue import Queue

class BPriorityQueue:
    # Creates an empty bounded priority queue.
    def __init__(self, numLevels):
        self.qSize = 0
        self.qLevels = Array(numLevels)
        for i in range(numLevels):
            self.qLevels.setItem(numLevels,Queue())

    # Return True if queue is empty
    def isEmpty(self):
        self.qLevels.__len__() == 0

    # Returns the number of items in the queue.
    def __len__(self):
        pass

    # Adds the given item to the queue
    def enqueue(self, item, priority):
        assert priority >= 0 and priority < len(self._qLevels), \
        "Invalid priority level."
        self.qLevels.elements[priority].enqueue(item)

    # Removes and returns the next item in the queue.
    def dequeue(self):
        # Make sure the queue is not empty.
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        i = 0
        p = self.qLevels.__len__()
        # Find the first non-empty queue.
        while i < p and not self.qLevels.elements[i].isEmpty():
            i += 1
        # We know the queue is not empty, so dequeue from the ith queue.
        return self.qLevels.elements[i].dequeue()