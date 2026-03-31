# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr = head
        prev = None
        newHead = None
        while ptr:
            if ptr.next == None:
                newHead = ptr
            next = ptr.next 
            ptr.next = prev

            prev = ptr
            ptr = next

        
        return newHead

