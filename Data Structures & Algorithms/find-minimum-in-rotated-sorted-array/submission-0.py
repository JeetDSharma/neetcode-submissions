class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)

        l,r=0,n-1
        ans = None
        count = 10
        while l<=r:
            m = l + (r-l)//2
            # print(l,m,r)
            # print(nums[l], nums[m], nums[r])
            # print()

            if nums[m] < nums[l]:
                r = m-1
                if ans is None:
                    ans=nums[m]
                ans = min(ans, nums[m])
            
            elif nums[m] > nums[r]:
                l = m+1
                if ans is None:
                    ans=nums[m]
                ans = min(ans, nums[m])
            
            else:
                r = m-1
                if ans is None:
                    ans=nums[m]
                ans = min(ans, nums[m])
            
            # print(ans)
            
            
        
        return ans
                