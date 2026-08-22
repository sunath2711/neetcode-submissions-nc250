class Node:
    def __init__(self, key:int, next_node=None):
        self.key = key
        self.next = next_node # this is important because before we unlink the current we set the next one for new node by this

class MyHashSet:

    def __init__(self):
        #choose a prime number here for key distribution
        self.size = 1009
        self.buckets = [Node(-1) for _ in range(self.size)]

    def _hash(self, key:int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        #below is find out which bucket our keywill go to - we assign the head to that bucket
        bucket_idx = self._hash(key)
        head = self.buckets[bucket_idx]

        #now that we have the head we want to add it at the right place
        new_node = Node(key, head.next)
        head.next = new_node

    def remove(self, key: int) -> None:
        bucket_idx = self._hash(key)
        curr = self.buckets[bucket_idx]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        
    def contains(self, key: int) -> bool:
        bucket_idx = self._hash(key)
        curr = self.buckets[bucket_idx]

        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)