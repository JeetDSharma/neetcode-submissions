class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        m,n=len(board), len(board[0])

        direction = [(0,1),(0,-1), (1,0), (-1,0)]

        for i in range(m):
            for j in range(n):
                s = [(i,j)]
                if board[i][j] == 'O' and (i,j) not in visited:
                    if i == 0 or j == 0 or i == m-1 or j == n-1:
                        continue
                    valid_region = True
                    # Here we do first pass and find that this is a
                    # valid region
                    temp_visited = visited.copy()
                    while s:
                        r,c = s.pop()
                        temp_visited.add((r,c))
                        for dr,dc in direction:
                            rn,cn = r+dr, c+dc

                            if rn<0 or cn<0 or rn>=m or cn>=n:
                                continue
                            
                            if board[rn][cn] == 'O':
                                if rn == 0 or cn == 0 or rn == m-1 or cn == n-1:
                                    valid_region = False
                                   
                                elif (rn,cn) not in temp_visited:
                                    s.append((rn,cn))
                         

                    # If valid region then let's do second pass
                    # Now we mark all O's as X's
                    if valid_region:
                        s = [(i,j)]
                        while s:
                            r,c = s.pop()
                            board[r][c] = 'X'
                            visited.add((r,c))
                            for dr,dc in direction:
                                rn,cn = r+dr, c+dc

                                if rn<0 or cn<0 or rn>=m or cn>=n:
                                    continue
                                print(board[rn][cn])
                                
                                if board[rn][cn] == 'O' and (rn,cn) not in visited:
                                    s.append((rn,cn))
                        
                    # After this update the visited state if 
                    # the case was for not valid region

                    visited = temp_visited.copy()

    

