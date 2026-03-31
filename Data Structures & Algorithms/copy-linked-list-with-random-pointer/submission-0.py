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
        # next -> new object
        # random -> new object, self, None

        # 0: Null
        # 1:  3
        # 2: 0
        # 3: 1

        # Object -> index mapping
        #index -> object 

        objectToIndex = {}
        indexToObject = {}

        ptr = head
        copyHead = None
        copyPtr = None
        i=0
        while ptr != None:
            objectToIndex[ptr] = i
            newNode = Node(ptr.val)
            if copyPtr != None:
                copyPtr.next = newNode
                copyPtr = newNode
            else:
                copyHead = newNode
                copyPtr = newNode
            indexToObject[i] = newNode
            ptr = ptr.next

            i+=1

        ptr = head
        copyPtr = copyHead
        while ptr != None:
            randomPtr = ptr.random
            if ptr.random != None:
                randomPtrIndex = objectToIndex[randomPtr]
                #get the object from the copy

                copyObjectRandom = indexToObject[randomPtrIndex]
                copyPtr.random = copyObjectRandom

            ptr = ptr.next
            copyPtr = copyPtr.next

        return copyHead

