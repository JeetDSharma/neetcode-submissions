class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slowPtr = nums[0]
        fastPtr = nums[slowPtr]

        while slowPtr != fastPtr:
            slowPtr = nums[slowPtr]
            fastPtr = nums[nums[fastPtr]]
        
        slowPtr = 0
        while slowPtr != fastPtr:
            slowPtr = nums[slowPtr]
            fastPtr = nums[fastPtr]
        
        return slowPtr