class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        #solve(i) represents the minimum cost to get to the ith stair
        # Base case here is if stair is below 0th then return 0 since it's cost is 0
        # Choice here is to come from one or two step back
        # The answr for solve(i) is the min of two choices
        
        memo = {}
        n = len(cost)
        cost.append(0)
        def solve(i):
            if i<0:
                return 0
            if i in memo:
                return memo[i]
            cost_one_step = solve(i-1) + cost[i]
            cost_two_step = solve(i-2) + cost[i]

            memo[i] = min(cost_one_step, cost_two_step)

            return memo[i]

        
        return solve(n)
