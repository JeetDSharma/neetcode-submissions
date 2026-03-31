class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_dict = {}

        ans = []
        word_freq = {}

        for s in strs:
            dic = {}
            for char in s:
                dic[char] = dic.get(char,0) + 1
            map_dict[s] = dic
            word_freq[s] = word_freq.get(s,0)+1
        
        # print(map_dict)
        print(word_freq)
        seen_set = set()
        for s in strs:
            if s not in seen_set:
                seen_set.add(s)
                sub_ans = [s]*word_freq[s]
                print(s)
                print(word_freq[s])
                s_dict = map_dict[s]
                for key, str_dict in map_dict.items():
                    if key == s:
                        continue
                    if str_dict == s_dict:
                        
                        seen_set.add(key)
                        sub_ans.append(key*word_freq[key])
                        
                ans.append(sub_ans)
        
        return ans
                    
