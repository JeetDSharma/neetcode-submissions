# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addValues(self, node1, node2, carry=0):
        sum = carry
        if node1:
            sum+=node1.val
        if node2:
            sum+=node2.val
        digit1 = sum%10
        carry = sum//10

        return digit1, carry
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l3_head = ListNode()
        l3 = l3_head
        while l1 or l2:
            digit1, carry = self.addValues(l1, l2, carry)
            print(digit1, carry)
            l3.next = ListNode(digit1)
            l3 = l3.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            l3.next = ListNode(carry)

        return l3_head.next
#      1     
#    5326
#     654
#     980