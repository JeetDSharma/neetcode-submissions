"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        objectMapping = {None: None}

        ptr = head

        while ptr:
            newNode = Node(ptr.val)
            objectMapping[ptr] = newNode
            ptr = ptr.next
        
        ptr = head
        while ptr:
            copy = objectMapping[ptr]
            copy.next = objectMapping[ptr.next]
            copy.random = objectMapping[ptr.random]
            ptr = ptr.next
        
        return objectMapping[head]

            
