class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n,m = len(board), len(board[0])

        for i in range(n):
            hash = {}
            for j in range(m):
                e = board[i][j]
                if e == ".":
                    continue
                if e in hash:
                    print(e, "row")
                    return False
                hash[e] = 1
        
        for j in range(m):
            hash = {}
            for i in range(n):
                e = board[i][j]
                if e == ".":
                    continue
                if e in hash:
                    print(e, "col")
                    return False
                hash[e] = 1
        
        iv,jv = 0,0
        for x in range(9):
            hash = {}
            i = iv
            for i in range(i,i+3):
                j=jv
                for j in range(j,j+3):
                    print(x,i,j)
                    e = board[i][j]
                    if e == ".":
                        continue
                    if e in hash:
                        print(e, "grid")
                        print(hash[e])
                        return False
                    hash[e] = 1
                

            jv+=3
            if x==2 or x==5:
                iv+=3
                jv=0

        return True


        
        
        