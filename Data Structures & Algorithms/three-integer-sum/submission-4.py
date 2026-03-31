from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lookupMap = defaultdict(int)

        n = len(nums)
        ans = set()

        for i in range(n):
            for j in range(i+1,n):
                lookup = - (nums[i]+nums[j])
                if lookup in lookupMap:
                    triplet = [nums[i],nums[j],lookup]
                    triplet.sort()
                    ans.add(tuple(triplet))
            lookupMap[nums[i]] = 1
        
        return [list(tup) for tup in ans]
                    