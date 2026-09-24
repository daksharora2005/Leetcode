class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        n=len(mat[0])
        m=len(mat)
        if m*n!=r*c:
            return mat
        new_mat=[[0 for _ in range(c)] for _ in range(r)]
        x=[]
        for i in range(m):
            for j in range(n):
                x.append(mat[i][j])
        k=0
        for i in range(r):
            for j in range(c):
                new_mat[i][j]=x[k]
                k+=1
        return new_mat
