# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        ptr = head
        while ptr!=None:
            size+=1
            ptr=ptr.next            
        if size == 1:
            return None
        c = 0
        ptr = head
        prev = None
        while c<size-n:
            prev = ptr
            ptr = ptr.next
            c+=1
        if not ptr.next:
            prev.next = None
        elif not prev:
            head = head.next
        else:
            prev.next = ptr.next
        
        return head

        