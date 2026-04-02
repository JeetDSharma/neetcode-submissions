class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        def backtrack(index=0, combination=[], combinationSum=0, depth=0):

            if combinationSum == target:
                result.append(combination.copy())
                return

            if index == len(candidates) or combinationSum > target:
                return
            
            elif combinationSum < target:

                combination.append(candidates[index])
                backtrack(index+1, combination, combinationSum+candidates[index], depth+1)
                combination.pop()
                
                cur = candidates[index]
                while index < len(candidates) and candidates[index] == cur:
                    index+=1

                backtrack(index, combination, combinationSum, depth+1)
        
        
        backtrack()

        return result
