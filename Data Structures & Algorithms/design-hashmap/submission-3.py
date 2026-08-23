class Node:

    def __init__(self,key: int = -1,value: int = -1, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node

class MyHashMap:

    def __init__(self):
        self.size = 1009
        self.buckets = [Node() for _ in range(self.size)] 

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        bucket_idx = self._hash(key)
        curr = self.buckets[bucket_idx].next

        #case 1 when key already present
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next

        #case 2 when key not present - we insert new node
        head = self.buckets[bucket_idx]
        new_node = Node(key, value, head.next)
        head.next = new_node

    def get(self, key: int) -> int:
        bucket_idx = self._hash(key)
        curr = self.buckets[bucket_idx].next # next to skip dummy head

        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        
        return -1

    def remove(self, key: int) -> None:
        bucket_idx = self._hash(key)
        curr = self.buckets[bucket_idx] # on dummy head
#here we traverse till the prior node of target node since we need the previous one for unlinking
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next               
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)