from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookupMap = {}

        for i,num in enumerate(nums):
            lookup = target-num
            if lookup in lookupMap:
                return [min(i,lookupMap[lookup]),max(i,lookupMap[lookup])]
            if num not in lookupMap:
                lookupMap[num] = i
        
