class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        l,r=0,0
        ans = 0
        while r<len(s):
            ss = s[r]
            freq[ss] += 1
            if freq[ss] > 1:
                while l<r and s[l] != ss:
                    freq[s[l]] -= 1
                    l+=1
                l+=1
                freq[ss] -= 1
            ans = max(r-l+1, ans)
            r+=1
            # print(freq, ans)
        
        return ans



        
