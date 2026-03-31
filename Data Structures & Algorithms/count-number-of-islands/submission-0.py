class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        print(n,m)
        visited = [[0 for _ in range(m)] for _ in range(n)]
        ans = 0
        def dfs(i,j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            
            if grid[i][j] == "0" or visited[i][j] == 1:
                return
            
            if grid[i][j] == "1":
                visited[i][j] = 1
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    ans += 1
                    dfs(i,j)
        
        return ans


        

                    





        