class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        l,r=0,n-1
        ans = [None,None]
        while l<=r:
            m = l + (r-l)//2
            # print(l,m,r)
            # print(nums[l], nums[m], nums[r])
            # print()

            if nums[m] < nums[l]:
                r = m-1
            elif nums[m] > nums[r]:
                l = m+1
            else:
                r = m-1
            
            if ans[0] is None:
                ans[0]=nums[m]
                ans[1] = m
            elif nums[m] < ans[0]:
                ans[0]=nums[m]
                ans[1] = m
            
        l,r=0,n-1
        if ans[1] != 0:
            if target >= nums[0]:
                r=ans[1]-1
            else:
                l = ans[1]
        
        while l<=r:
            m = l + (r-l)//2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        
        return -1
                