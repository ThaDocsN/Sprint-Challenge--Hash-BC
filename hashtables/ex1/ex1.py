#  Hint:  You may not need all of these.  Remove the unused functions.
# from hashtables import (HashTable,
#                         hash_table_insert,
#                         hash_table_remove,
#                         hash_table_retrieve,
#                         hash_table_resize)

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# Hash int
def hash(x, max):
    x = ((x >> 16) ^ x) * 0x45d9f3b
    x = ((x >> 16) ^ x) * 0x45d9f3b
    x = ((x >> 16) ^ x)

    return x % max


# '''
# Fill this in.

# Hint: Used the LL handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, len(hash_table.storage))

    current_pair = hash_table.storage[index]
    last_pair = None

    while current_pair is not None and current_pair.key != key:
        last_pair = current_pair
        current_pair = last_pair.next

    if current_pair is not None:
        current_pair.value = value
    else:
        new_pair = LinkedPair(key, value)
        new_pair.next = hash_table.storage[index]
        hash_table.storage[index] = new_pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, len(hash_table.storage))

    current_pair = hash_table.storage[index]
    last_pair = None

    while current_pair is not None and current_pair.key != key:
        last_pair = current_pair
        current_pair = last_pair.next

    if current_pair is None:
        print("ERROR: Unable to remove entry with key " + key)
    else:
        if last_pair is None:  # Removing the first element in the LL
            hash_table.storage[index] = current_pair.next
        else:
            last_pair.next = current_pair.next


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, len(hash_table.storage))

    current_pair = hash_table.storage[index]

    while current_pair is not None:
        if(current_pair.key == key):
            return current_pair.value
        current_pair = current_pair.next


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_hash_table = HashTable(2 * len(hash_table.storage))

    current_pair = None

    for i in range(len(hash_table.storage)):
        current_pair = hash_table.storage[i]
        while current_pair is not None:
            hash_table_insert(new_hash_table,
                              current_pair.key,
                              current_pair.value)
            current_pair = current_pair.next

    return new_hash_table

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    for j in range(length):
        k = hash_table_retrieve(ht, limit - weights[j])
        if k is not None:
            return (j, k) if j > k else (k, j)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
