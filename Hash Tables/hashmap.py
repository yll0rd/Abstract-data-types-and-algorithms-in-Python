from Array_module.arrayADT import Array


class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# Defines constants to represent the status of each table entry.
UNUSED = None
EMPTY = _MapEntry(None, None)


class HashMap:
    # Creates an empty map instance.
    def __init__(self):
        self._table = Array(7)
        self._count = 0
        self._maxCount = self._table.__len__() - (self._table.__len__() // 3)

    # Returns the number of entries in the map.
    def __len__(self):
        return self._count

    # Determines if the map contains the given key
    def __contains__(self, key):
        slot = self._findSlot(key, False)
        return slot is not None

    # Adds a new entry to the map if the key does not exist. Otherwise, the
    # new value replaces the current value associated with the key.
    def add(self, key, value):
        if self.__contains__(key):
            slot = self._findSlot(key, False)
            self._table.elements[slot].value = value
            return False
        else:
            slot = self._findSlot(key, True)
            self._table.elements[slot] = _MapEntry(key, value)
            self._count += 1
            if self._count == self._maxCount:
                self._rehash()
            return True

    def valueOf(self, key):
        slot = self._findSlot(key, False)
        assert slot is not None, "Invalid map key."
        return self._table.elements[slot].value

    # Finds the slot containing the key or where the key can be added.
    # forInsert indicates if the search is for an insertion, which locates
    # the slot into which the new key can be added.
    def _findSlot(self, key, forInsert):
        # Compute the home slot and the step size.
        slot = self._hash1(key)
        step = self._hash2(key)

        # Probe for key.
        M = self._table.__len__()
        while self._table.elements[slot] is not UNUSED:
            if forInsert and \
                    self._table.elements[slot] is UNUSED or self._table.elements[slot] is EMPTY:
                return slot
            elif not forInsert and \
                    (self._table.elements[slot] is not EMPTY and self._table.elements[slot].key == key):
                return slot
            else:
                slot = (slot + step) % M

    # Rebuilds the hash table
    def _rehash(self):
        # Create a new larger table
        origTable = self._table
        newSize = self._table.__len__() * 2 + 1
        self._table = Array(newSize)

        # Modify the size attributes
        self._count = 0
        self._maxCount = newSize - (newSize // 3)

        # Add the keys from the original to the new table
        for entry in origTable:
            if entry is not UNUSED and entry is not EMPTY:
                slot = self._findSlot(entry.key, True)
                self._table.setItem(slot, entry.value)
                self._count += 1

    # The main hash function for mapping keys to table entries.
    def _hash1(self, key):
        return abs(hash(key) % self.__len__())

    # The second hash function used with double hashing probes.
    def _hash2(self, key):
        return 1 + abs(hash(key) % self._table.__len__() - 2)
