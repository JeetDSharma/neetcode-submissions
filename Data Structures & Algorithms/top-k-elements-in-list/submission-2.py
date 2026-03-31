from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        sorted_dict = sorted(freq.items(), key = lambda x: x[1], reverse=True)
        
        top_k = [key for key,val in sorted_dict]

        # print(top_k) 
        
        return top_k[:k]


        
        

