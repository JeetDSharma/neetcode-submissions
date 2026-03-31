class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = [0 for _ in range(26)]
        freq_t = [0 for _ in range(26)]

        for char in s:
            char_index = ord(char) - ord('a')
            freq_s[char_index] += 1
        for char in t:
            char_index = ord(char) - ord('a')
            freq_t[char_index] += 1
        
        if freq_s == freq_t:
            return True
        return False
            