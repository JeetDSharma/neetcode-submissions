from collections import defaultdict
class Solution:
    

    def checkInclusion(self, s1: str, s2: str) -> bool:
        charMap2 = defaultdict(int)
        charMap1 = defaultdict(int)
        for char in s1:
            charMap1[char] += 1

        p1,p2=0,0
        n1=len(s1)
        n2=len(s2)
        if n2<n1:
            return False
        while p2-p1 < n1-1:
            charMap2[s2[p2]]+=1
            p2+=1
        # for char,count in charMap2.items():
        #     print(char,count)
        while p2<n2:
            charMap2[s2[p2]]+=1
            for char,count in charMap2.items():
                print(char,count)
            print()
            if charMap1 == charMap2:
                return True
            if charMap2[s2[p1]]-1<=0:
                del charMap2[s2[p1]]
            else:
                charMap2[s2[p1]] -=1
            p1+=1
            p2+=1
        
        return False
            

    