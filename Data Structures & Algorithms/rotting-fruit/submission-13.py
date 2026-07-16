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
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        while q:
            i,j,depth = q.popleft()
            max_depth = max(max_depth,depth)
            # print(i,j, count_fresh)
            for dc,dr in directions:
                c,r = i+dc, j+dr
                
                if valid_cell(c,r) and (c,r) not in visited:
                    q.append((c,r,depth+1))
                    visited.add((c,r))
                    count_fresh -= 1

        if count_fresh == 0:
            return max_depth
        
        return -1
        
            

            