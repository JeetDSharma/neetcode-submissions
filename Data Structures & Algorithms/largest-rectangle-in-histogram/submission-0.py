class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [(heights[0],0)]
        area = [0]*n

        for i in range(1,n):
            if stack and heights[i] >= stack[-1][0]:
                stack.append((heights[i],i))

            else:
                count = 0
                while stack and heights[i] < stack[-1][0]:
                    popped = stack.pop()
                    count+=1
                    area[popped[1]] += popped[0]*count
                
                for entry in stack:
                    area[entry[1]] += count*entry[0]
                stack.append((heights[i],i))

        count = 0
        while stack:
            popped = stack.pop()
            count+=1
            area[popped[1]] += popped[0]*count

        stack = [(heights[n-1],n-1)]
        for i in reversed(range(0,n-1)):
            if stack and heights[i] >= stack[-1][0]:
                stack.append((heights[i],i))

            else:
                count = 0
                while stack and heights[i] < stack[-1][0]:
                    popped = stack.pop()
                    count+=1
                    area[popped[1]] += popped[0]*count
                
                for entry in stack:
                    area[entry[1]] += count*entry[0]
                stack.append((heights[i],i))

        count = 0
        while stack:
            popped = stack.pop()
            count+=1
            area[popped[1]] += popped[0]*count


        max_area = 0
        for i in range(0,n):
            max_area = max(max_area,area[i]-heights[i])

        return max_area



            
        

