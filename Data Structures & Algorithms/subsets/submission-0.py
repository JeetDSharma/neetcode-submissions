class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        def backtrack(index, ans=[]):
            if index == len(nums):
                return

            ans.append(nums[index])

            result.append(ans.copy())
            backtrack(index+1, ans)
            ans.pop()

            backtrack(index+1, ans)
            
       
        backtrack(0)

        return result