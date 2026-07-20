class Solution:
    def rob(self, nums: List[int]) -> int:
        

        # solve(i) represents the max profit I can attain after robbing the best possible houses till ith
        n = len(nums)
        # can_rob = [True for _ in range(n)]
        memo = {}
        def solve(i):

            if i == 0:
                return nums[i]
            if i < 0:
                return 0
                
            if i in memo:
                return memo[i]

            choice1 = nums[i] + solve(i-2)
                
            choice2 = solve(i-1)
            

            memo[i] = max(choice1, choice2)

            return memo[i]
          
        
        return solve(n-1)