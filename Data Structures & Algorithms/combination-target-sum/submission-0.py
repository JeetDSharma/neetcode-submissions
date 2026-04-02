class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        def backtrack(index=0, combination=[], combinationSum=0):
            if index == len(nums):
                return
            
            if combinationSum + nums[index] == target:
                combination.append(nums[index])
                result.append(combination.copy())
                combination.pop()
                
            
            elif combinationSum + nums[index] < target:
                combinationSum += nums[index]
                combination.append(nums[index])
                backtrack(index, combination, combinationSum)
                combination.pop()
                combinationSum -= nums[index]
                backtrack(index+1, combination, combinationSum)
            
        backtrack()
        return result