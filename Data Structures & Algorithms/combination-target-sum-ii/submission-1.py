class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        seen = set()
        def backtrack(index=0, combination=[], combinationSum=0, depth=0):

            if tuple(combination) in seen:
                return

            if combinationSum == target:
                result.append(combination.copy())


            if index == len(candidates) or combinationSum > target:
                return
            
            elif combinationSum < target:

                combination.append(candidates[index])
                backtrack(index+1, combination, combinationSum+candidates[index], depth+1)
                seen.add(tuple(combination))
                combination.pop()
                backtrack(index+1, combination, combinationSum, depth+1)
                seen.add(tuple(combination))

        
        backtrack()

        return result
