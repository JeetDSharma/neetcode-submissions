class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        n = len(temperatures)
        ans = [0]*n
        for i in range(1,n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                top_idx = stack.pop()
                ans[top_idx] = i-top_idx
            stack.append(i)

        return ans
