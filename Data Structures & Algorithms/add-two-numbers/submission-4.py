# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
2591
38955

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1:
            return l2
        if not l2:
            return l1
        
        l3_head = None
        l3 = None
        carry = None
        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if carry:
                sum += carry

            digit = sum%10
            carry = sum//10
            
                    
            new_node = ListNode(val=digit)

            if not l3:
                l3 = new_node
                l3_head = l3
            else:
                l3.next = new_node
                l3=l3.next
        if carry:
            l3.next = ListNode(val=carry)
        return l3_head

            

        