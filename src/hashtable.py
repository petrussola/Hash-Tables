# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.usage = 0
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # start from an arbitrary large prime such as (5381)
        # set the ahs value to 5381
        hash = 5381
        # iterate over each char in the key
        for el in key:
            # set the hash value to the bit shift left by 5 of the hash value and sum of the hash value  then add the value for the char
            hash = ((hash << 5) + hash) + ord(el)
        # return the hash value
        return hash

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if not self.storage[index]:
            self.storage[index] = LinkedPair(key, value)
            self.usage += 1
        else:
            node = self.storage[index]
            while node:
                if node.key == key:
                    node.value = value
                    return value
                else:
                    prev_node = node
                    node = node.next
            prev_node.next = LinkedPair(key, value)
        # load factor
        load_factor = self.usage / len(self.storage)

        if load_factor > 0.7:
            self.resize(16)
        elif load_factor < 0.2:
            self.resize(4)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if not self.storage[index]:
            print("No data to be deleted")
        else:
            # if the node at index is the last one, set the index to None value
            node = self.storage[index]
            if not node.next:
                self.storage[index] = None
                self.usage -= 1

            # if it is not the last one, loop over the LL to find the node with the key we are looking for
            else:
                while node.key != key:
                    prev_node = node
                    node = node.next
            # when we find it
            # if it is the last one, set the previous node next to none
            # if it isn't, link previous node next to the next node after the one with the key we are looking for
                prev_node.next = node.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        while node:
            if node.key == key:
                return node.value
            else:
                node = node.next

    def resize(self, factor):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = factor
        new_storage = [None] * factor
        for i in range(self.usage):
            new_storage[i] = self.storage[i]
        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
