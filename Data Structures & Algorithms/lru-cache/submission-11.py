class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def _insert(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.hashMap:
            curNode = self.hashMap[key]
            self._remove(curNode)
            self._insert(curNode)
            return self.hashMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        newNode = Node(key,value)
        if key in self.hashMap:
            curNode = self.hashMap[key]
            self._remove(curNode)
            self.hashMap[key] = newNode 

        self._insert(newNode)
        self.hashMap[key] = newNode

        if len(self.hashMap) > self.capacity:
            # print("Removing: ", )
            del self.hashMap[self.left.next.key]
            self._remove(self.left.next)


        

        
