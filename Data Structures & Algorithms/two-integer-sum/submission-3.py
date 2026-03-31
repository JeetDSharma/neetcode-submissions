from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = defaultdict(list)

        for i,num in enumerate(nums):
            index_map[num].append(i)
        
        ans = [10**18,10**18]
        for i,num in enumerate(nums):
            lookup = target-num
            if lookup in index_map:
                lowest_index = None
                for idx in index_map[lookup]:
                    if idx == i:
                        continue
                    if lowest_index == None:
                        lowest_index = idx
                    elif idx < lowest_index:
                        lowest_index = idx
                if lowest_index is not None:
                    l,r = min(i,lowest_index),max(i,lowest_index)
                    if l<ans[0]:
                        ans = [l,r]
        return ans