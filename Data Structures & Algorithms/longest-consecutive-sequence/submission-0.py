from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = {}
        ans = 0
        for num in nums:
            visited[num] = False
        
        def calcConsecutiveRight(num,ans=0):
            if num not in visited or visited[num]:
                return ans

            visited[num] = True
            ans += calcConsecutiveRight(num+1,ans)
            return ans+1
           

        def calcConsecutiveLeft(num,ans = 0):
            if num not in visited or visited[num]:
                return ans

            visited[num] = True
            ans += calcConsecutiveLeft(num-1,ans)
            
            return ans+1
            
        
        for num in nums:
            ans = max(ans, calcConsecutiveLeft(num-1)+calcConsecutiveRight(num+1)+1)
            visited[num] = True
            

        return ans
        
    

