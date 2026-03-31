class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0 for _ in range(n)]

        stack = []

        for cur_index,temp in enumerate(temperatures):
            if len(stack)==0:
                stack.append(cur_index)
            elif temp <= temperatures[stack[-1]]:
                stack.append(cur_index)
            else:
                while stack and temp > temperatures[stack[-1]]:
                    day_index = stack[-1]
                    days_to_wait = cur_index-day_index
                    ans[day_index] = days_to_wait
                    stack.pop()
                stack.append(cur_index)
        
        return ans
