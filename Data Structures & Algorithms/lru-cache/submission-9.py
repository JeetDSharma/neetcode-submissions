from collections import defaultdict
class Node:
    def __init__(self, key, value, next=None, prev=None):
        self.val = value
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    #This inserts a node to right (Most recent Used)
    def insert(self, node):
        self.right.prev.next, node.prev  = node, self.right.prev
        node.next = self.right
        self.right.prev = node

    #This removes a node from the ll
    def remove(self, node):
        node.prev.next, node.next.prev = node.next,  node.prev

    def get(self, key: int) -> int:
        if key in self.cache:  
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            print(self.right.prev.key)
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        newNode = Node(key, value)
        self.insert(newNode)
        
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = newNode
        
        # for key,val in self.cache.items():
        #     print(key, val.val)
        # print()
        if len(self.cache) > self.capacity:
            # print("deleting: ", self.left.next.key)
            del self.cache[self.left.next.key]
            self.remove(self.left.next)


        





