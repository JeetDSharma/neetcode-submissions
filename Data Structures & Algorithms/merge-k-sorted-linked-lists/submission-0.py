# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
import itertools
# from collections import defaultdict


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        

    #     O(1) figure out where to insert it
    #     Hashmap??

    #     O(n) possible??


    #    1 -> 2 -> 4
    #    1  ---> 3 -> 5
    #            3 ----> 6


    #     k-pointers to compare initially

    #     pick the smallest of these k pointers, and make it my head of ans

    #     at max have k pointers in memory, we can put them in a list, take min, and replace with next pointer or None, or delete it, hmm

    #     I need a efficient O(1) min find

    #     So I use a min heap with at max k elements, log(k) insertion and deletion so time: n*log(k) and O(1) retrievval and space is O(k)

    #     Does not sound that bad to me. 

    #     Seems easy to implement, we can also have lazy deletion. 

    # What is a min heap? I use heapq from collections and maintain a count variable
    # heappush and pop is there and get min is there, and count to pop if it is zero

    
        hq = []
        # count = defaultdict(int)
        head = None
        ptr = None
        counter = itertools.count()

        for node in lists:
            heapq.heappush(hq,(node.val,next(counter),node))
            # count[node.val] += 1
        
        while hq:
            if head is None:
                head = hq[0][2]
                ptr = head
            else:
                ptr.next = hq[0][2]
                ptr = hq[0][2]

            poped_element = heapq.heappop(hq)

            if poped_element[2].next:
                node = poped_element[2].next
                heapq.heappush(hq,(node.val,next(counter),node))
        
        return head

    # [1,1,3]



    

    
         

        