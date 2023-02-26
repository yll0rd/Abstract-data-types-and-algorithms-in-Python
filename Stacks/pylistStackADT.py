class Stack():
    def __init__(self):
        self.theItems = list()

    def isEmpty(self):
        return len(self.theItems) == 0
    
    def size(self):
        return len(self.theItems)
    
    def push(self, item):
        self.theItems.append(item)

    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        self.theItems.pop(-1)

    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self.theItems[-1]