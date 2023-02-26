class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head is None
    
    def __len__(self):
        return self.size
    
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack." 

    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        self.head = self.head.next
        self.size -= 1

    def push(self, item):
        self.head = StackNode(item, self.head)
        self.size += 1

class StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link