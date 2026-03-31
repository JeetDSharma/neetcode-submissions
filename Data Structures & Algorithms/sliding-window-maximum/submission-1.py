from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ## This time we will be using the Monotonic Deque

        n=len(nums)
        dq = deque()
        ans = []
        r = 0
        while r<n:
            while dq and nums[dq[-1]] <= nums[r]:
                # print("poped: ",dq[-1])
                dq.pop()
            
            dq.append(r)
            # print("appended: ", r)
            if dq[0] <= r-k:
                dq.popleft()
            
            if r >= k-1:
                ans.append(nums[dq[0]])

            
            r+=1
            
        return ans


        