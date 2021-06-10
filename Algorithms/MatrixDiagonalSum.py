    def diagonalSum(mat):
        if len(mat) == 1:
            return mat[0][0]
        
        count = 0 
        for i in range(len(mat)):
            count += mat[i][i]
            count += mat[i][-1-i]
            
        if len(mat) % 2 == 1:
            count -= mat[len(mat)//2][len(mat)//2]
        
        return count
