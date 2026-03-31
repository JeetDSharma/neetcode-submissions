from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # freq_buckets = [[0 for _ in range(26)]  for _ in range(len(strs))]

        # groups = [[] for _ in range(len(strs))]

        # for i, string in enumerate(strs):
        #     char_freq = [0 for _ in range(26)]
        #     for char in string:
        #         char_index = ord(char)-ord('a')
        #         char_freq[char_index] += 1
            
        freq_bucket = defaultdict(list)
        for string in strs:
            char_freq = [0 for _ in range(26)]
            for char in string:
                char_index = ord(char) - ord('a')
                char_freq[char_index] += 1
            freq_bucket[tuple(char_freq)].append(string)
        
        return list(freq_bucket.values())
