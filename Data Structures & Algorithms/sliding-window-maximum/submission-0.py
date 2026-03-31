import heapq
class Solution:
    def __init__(self):
        self.heap = []
        self.count = {}
    def add_element(self,x):
        x= -x
        heapq.heappush(self.heap,x)
        self.count[x] = self.count.get(x,0)+1
    def get_max(self):
        while self.count[self.heap[0]] == 0:
            heapq.heappop(self.heap)
        return -self.heap[0]
    def remove_element(self,x):
        x = -x
        self.count[x] -= 1
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 7 5 2 3 2 4 6
        # keep track of all elements in window size: eg->100

        # I can maintain a sort of sorted hashMap so that
        # I can access the top element in O(1) time, 
        # which makes time complexity O(N*log(M))
        # as we encounter a element, add it to our hashMap
        # when we are at our window size, pick the top element from hashMap
        # Add and remove element freq as we traverse the array

        #So what I understood is that I need to use something like
        #a min-heap in python with (negation trick) to make it a 
        #max-heap

        l,r=0,0
        n = len(nums)
        ans = []
        while r<n:
            self.add_element(nums[r])
            if r-l+1 == k:
                ans.append(self.get_max())
                self.remove_element(nums[l])
                l+=1
            r+=1

        return ans

