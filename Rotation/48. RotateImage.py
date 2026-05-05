class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            for j in range(0, n//2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
        
    #a00 a20
    #a01 a21
    a10
    #a02 a22

    #a10 a01
    #a11 a11
    #a12 a21

    #a20 a00
    #a21 a01
    #a22 a02

    
#a00 = 1 4 7
#a01 = 2 5 8 
#a20 = 3 6 9