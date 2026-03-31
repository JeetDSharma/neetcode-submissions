class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for string in strs:
            sorted_string = "".join(sorted(string))
            anagram[sorted_string].append(string)

        
        return list(anagram.values())