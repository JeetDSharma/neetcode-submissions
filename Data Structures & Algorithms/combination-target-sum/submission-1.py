class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        def backtrack(index=0, combination=[], combinationSum=0):
            if index == len(nums) or combinationSum > target:
                return
            
            if combinationSum == target:
                result.append(combination.copy())
                
            
            elif combinationSum < target:
                combinationSum += nums[index]
                combination.append(nums[index])
                backtrack(index, combination, combinationSum)
                combination.pop()
                combinationSum -= nums[index]
                backtrack(index+1, combination, combinationSum)
            
        backtrack()
        return result