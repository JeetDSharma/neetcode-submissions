class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0, n-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            elif target <= nums[m]:
                r = m-1
            else:
                l = m+1
        return -1
