import copy
class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """

        
        refMat=[[0 for _ in range(len(target[0]))] for _ in range(len(target))]

        if mat==target:
            return True

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                refMat[i][j]=target[i][j]

        newMat=[[0 for _ in range(len(target[0]))] for _ in range(len(target))]

        for _ in range(3):
            for i in range(len(newMat)):
                for j in range(len(newMat[0])):
                    newMat[i][j]=refMat[j][len(refMat)-1-i]

            if newMat ==mat:
                return True
            else :
                refMat=copy.deepcopy(newMat)
        return False


        