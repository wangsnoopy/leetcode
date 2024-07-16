class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # find all 0 in the oridinal matrix
        zero_r = []
        zero_c = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in zero_r:
                        zero_r.append(i)
                    if j not in zero_c:
                        zero_c.append(j)
        
        # set the entire row and column to zero
        # ex: (1,1) is the zero, so row 1 and column 1 must all be zero
        for i in range(m):
            for j in range(n):
                if i in zero_r or j in zero_c:
                    matrix[i][j] = 0