from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])

        count_fresh = 0
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count_fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j,0))
        def valid_cell(i,j) -> bool:
            
            if i<0 or j<0 or i>=n or j>=m:
                return False
            
            elif grid[i][j] == 0 or grid[i][j] == 2:
                return False
            return True

        max_depth = 0
        visited = set()
        while q:
            i,j,depth = q.popleft()
            max_depth = max(max_depth,depth)
            # print(i,j, count_fresh)
            if valid_cell(i+1,j) and (i+1,j) not in visited:
                q.append((i+1,j,depth+1))
                visited.add((i+1,j))
                count_fresh -= 1
            if valid_cell(i-1,j) and (i-1,j) not in visited:
                q.append((i-1,j,depth+1))
                visited.add((i-1,j))
                count_fresh -= 1
            if valid_cell(i,j+1) and (i,j+1) not in visited:
                q.append((i,j+1,depth+1))
                visited.add((i,j+1))
                count_fresh -= 1
            if valid_cell(i,j-1) and (i,j-1) not in visited:
                q.append((i,j-1,depth+1))
                visited.add((i,j-1))
                count_fresh -= 1
        

        print(count_fresh)
        if count_fresh == 0:
            return max_depth
        
        return -1
        
            

            