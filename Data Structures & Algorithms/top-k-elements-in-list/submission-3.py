from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        buckets = defaultdict(list)

        for key,val in freq.items():
            buckets[val].append(key)
        
        i = len(nums)
        top_k = []
        while i>0:
            if i in buckets:
                top_k.extend(buckets[i])
            
            if len(top_k) >= k:
                break
            i-=1

        return top_k

        
        