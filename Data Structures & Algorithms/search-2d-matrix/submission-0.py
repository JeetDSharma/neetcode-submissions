class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, m*n-1

        while l<=r:
            print(l,r)
            mid = l+(r-l)//2
            print(mid)
            i,j = self.ind(mid, m)
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                l=mid+1
            else:
                r=mid-1
        return False

    def ind(self,num, m):
        if num%m == m:
            return 0, num
        else:
            return  num//m, num%m


