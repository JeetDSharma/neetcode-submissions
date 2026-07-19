class Solution:
    def climbStairs(self, n: int) -> int:

        # What does i represent?
        # here it represetns the number of ways to climb the stairs

        # What is the choice here?
        # Here I have to calculate how many ways to climb previous two stairs, it's not a choice per se
        # s1 = solve(i-1) s2 = solve(i-2)

        # What is base case here
        # Base case is when i == 1 or i == 2 return 1 or 2 respectively

        # what do we return
        # We return s1+s2
        memo = [0 for _ in range(n+1)]

        def solve(n):
            if n == 2:
                return 2
            if n == 1:
                return 1
            if memo[n] > 0:
                return memo[n]

            one_step_back = solve(n - 1)
            two_step_back = solve(n - 2)
            memo[n] = one_step_back + two_step_back
            return memo[n]

        return solve(n)
