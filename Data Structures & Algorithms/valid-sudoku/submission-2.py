from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n,m = len(board), len(board[0])
        rowMap=defaultdict(list)
        colMap=defaultdict(list)
        gridMap = defaultdict(list)
        for i in range(n):
            for j in range(m):
                e = board[i][j]
                # print(e,i,j)
                if e == ".":
                    continue
                if e in rowMap[i]:
                    return False
                if e in colMap[j]:
                    return False
                if e in gridMap[i//3*3+j//3]:
                    return False
                rowMap[i].append(e)
                colMap[j].append(e)
                gridMap[i//3*3+j//3].append(e)
        return True


        
        
        