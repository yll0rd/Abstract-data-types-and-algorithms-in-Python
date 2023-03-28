from Arrays.arrayADT import Array


# An array-based implementation of the max heap
class MaxHeap:
    # Create a max-heap with maximum capacity of maxSize.
    def __init__(self, maxSize):
        self._elements = Array(maxSize)
        self._count = 0

    # Return the number of items in the heap
    def __len__(self):
        return self._count

    # Create a max-heap with maximum capacity of maxSize.
    def capacity(self):
        return len(self._elements)

    # Add a new value to the heap.
    def add(self, value):
        assert self._count < self.capacity(), "Cannot add to a full heap."
        # Add the new value to the end of the list.
        self._elements[self._count] = value
        self._count += 1
        # Sift the new value up the tree.
        self._siftUp(self._count - 1)

    # Extract the maximum value from the heap
    def extract(self):
        assert self._count > 0, "Cannot extract from an empty heap."
        # Save the root value and copy the last heap value to the root.
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        # Sift the root value down the tree.
        self._siftDown(0)

    # Sift the value at the ndx element up the tree.
    def _siftUp(self, ndx):
        if ndx > 0:
            parent = ndx // 2
            if self._elements[ndx] > self._elements[parent]:  # Swap elements
                self._elements[ndx], self._elements[parent] = \
                    self._elements[parent], self._elements[ndx]
                self._siftUp(parent)

    # Sift the value at the ndx element down the tree.
    def _siftDown(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        # Determine which node contains the larger value
        largest = ndx
        if left < self._count and self._elements[left] >= self._elements[largest]:
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = left
        # If the largest value is not in the current node (ndx), swap it with
        # the largest value and repeat the process.
        if largest != ndx:
            self._elements[ndx], self._elements[largest] = \
                self._elements[largest], self._elements[ndx]
            self._siftDown(largest)
