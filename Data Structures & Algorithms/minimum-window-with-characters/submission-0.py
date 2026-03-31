from collections import defaultdict
class Solution:
    def compareMap(self,map1,map2):
        for key, val in map2.items():
            if key not in map1:
                return False
            if map1[key] < map2[key]:
                return False
        return True 
    def minWindow(self, s: str, t: str) -> str:
        tMap = defaultdict(int)
        stMap = defaultdict(int)
        sMap = defaultdict(int)
        
        for char in t:
            tMap[char] += 1
        
        l,r=0,0
        ans = ""
        ansLen = math.pow(10,4)
        while r<len(s):
            if s[r] in tMap:
                stMap[s[r]] += 1

            else:
                sMap[s[r]] += 1 

            print(stMap, sMap)
            while self.compareMap(stMap,tMap) and l<=r:
                print(l,r)
                if len(s[l:r+1]) < ansLen:
                    ans = s[l:r+1]
                    ansLen = len(s[l:r+1])
                mapToDecrement = stMap if s[l] in stMap else sMap
                
                if mapToDecrement[s[l]] > 1:
                    mapToDecrement[s[l]] -= 1
                else:
                    del mapToDecrement[s[l]]
                
                l+=1
                    
            r+=1
        # print(l,r)
        # while compareMap(stMap,tMap) and l<=r:
        #     print(l,r)
        #     if len(s[l:r+1]) < ansLen:
        #         ans = s[l:r+1]
        #         ansLen = len(s[l:r+1])
        #     mapToDecrement = stMap if s[l] in stMap else sMap
            
        #     if mapToDecrement[s[l]] > 1:
        #         mapToDecrement[s[l]] -= 1
        #     else:
        #         del mapToDecrement[s[l]]
            
        #     l+=1
        return ans