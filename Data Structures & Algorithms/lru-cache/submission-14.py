class Node:
    def __init__(self, prev = None, next = None, val=None):
        self.prev = prev
        self.next = next
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.start = Node()
        self.end = Node()

        self.start.next = self.end
        self.end.prev = self.start
    
    def add_node(self,node):
        prev = self.end.prev
        prev.next = node
        node.prev = prev
        node.next = self.end
        self.end.prev = node
    
    def remove_node(self,node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.mapping:
            cur_node = self.mapping[key]
            val = cur_node.val[1]
            self.remove_node(cur_node)
            self.add_node(cur_node)
            return val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        new_node = Node(val = [key, value])
        if key in self.mapping:
            self.remove_node(self.mapping[key])
            self.add_node(new_node)
            self.mapping[key] = new_node
        else:
            self.add_node(new_node)
            self.mapping[key] = new_node
            self.capacity -= 1
        
            if self.capacity < 0:
                del self.mapping[self.start.next.val[0]]
                self.remove_node(self.start.next)
            


        
