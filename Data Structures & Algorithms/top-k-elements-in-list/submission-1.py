from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)

        for num in nums:
            freqMap[num] += 1

        n = len(nums)
        freqArr = [[] for x in range(n+1)] 

        for num, freq, in freqMap.items():
            # print('indedxing freq: ', freq)
            # print('indexing element: ',num)
            freqArr[freq].append(num)
        
        ans = []
        i= n
        while k:
            if len(freqArr[i]):
                # print('freq: ', i)
                # print("element: ", freqArr[i])
                ans.extend(freqArr[i])
            
            if len(ans) >= k:
                break
            
            i-=1
        
        return ans


