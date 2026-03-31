class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        
        ans = [intervals[0]]
        for i in range(1,n):
            l = ans[-1]
            r = intervals[i]
            
            if l[1] >= r[0]:
                ans.pop()
                if l[1] < r[1]:
                    ans.append([l[0], r[1]])
                else:
                    ans.append([l[0], l[1]])
            else:
                ans.append(r)

        return ans