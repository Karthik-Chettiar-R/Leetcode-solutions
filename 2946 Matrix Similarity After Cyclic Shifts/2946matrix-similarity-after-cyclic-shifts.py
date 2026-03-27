def leftShift(matrix,k,result,row):
    size=len(matrix[0])
    k%=size
    for i in range(len(matrix[row])):
        result[row][i]=matrix[row][(i+k)%size]
def rightShift(matrix,k,result,row):
    size=len(matrix[0])
    k%=size
    for i in range(len(matrix[row])):
        result[row][i]=matrix[row][(i-k)%size]




class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        result=[[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for i in range(len(mat)):
            if i%2==0:
                leftShift(mat,k,result,i)
            else :
                rightShift(mat,k,result,i)
        return result==mat

        

