class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_dict = defaultdict(list)


        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char)-ord("a")] += 1
            map_dict[tuple(count)].append(word)
        
        return list(map_dict.values())
                    
