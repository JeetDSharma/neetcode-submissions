from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid), len(grid[0])

        non_traversable = {-1, 0}

        def in_bound(i: int,j: int) -> bool:
            if i<0 or j<0:
                return False
            if i>=m or j>=n:
                return False
            if grid[i][j] == -1:
                return False
            return True

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if val not in non_traversable:
                    q = deque([(i,j,0)])
                    
                    visited = set((i,j))
                    
                    while q:
                        r,c,dist = q.popleft()
                        if grid[r][c] == 0:
                            grid[i][j] = dist
                            break
                        if in_bound(r,c+1) and (r,c+1) not in visited:
                            q.append((r,c+1,dist+1))
                            visited.add((r,c+1))
                        
                        if in_bound(r+1,c) and (r+1,c) not in visited:
                            q.append((r+1,c,dist+1))
                            visited.add((r+1,c))
                        if in_bound(r-1,c) and (r-1,c) not in visited:
                            q.append((r-1,c,dist+1))
                            visited.add((r-1,c))
                        
                        if in_bound(r,c-1) and (r,c-1) not in visited:
                            q.append((r,c-1,dist+1))
                            visited.add((r,c-1))
        
       





