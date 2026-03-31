# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        if not list1:
            return list2
        
        if list2.val < list1.val:
            list1,list2 = list2, list1
        
        newList = list1
        newHead = list1
        list1 = list1.next

        while list1 and list2:
            if list2.val < list1.val:
                list1,list2 = list2, list1
            
            newList.next = list1
            newList = list1
            list1 = list1.next
        
        while list1:
            newList.next = list1
            newList = list1
            list1 = list1.next
        
        
        while list2:
            newList.next = list2
            newList = list2
            list2 = list2.next
        
        return newHead