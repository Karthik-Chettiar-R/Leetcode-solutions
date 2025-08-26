import math
class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        max=0
        index=0
        cur=0
        for i in range(len(dimensions)):
            
                    
            if (dimensions[i][0]**2+dimensions[i][1]**2)>cur:
                cur=dimensions[i][0]**2 +dimensions[i][1]**2
                index=i
                max=(dimensions[i][0]*dimensions[i][1])
            elif cur==(dimensions[i][0]**2+dimensions[i][1]**2):
                if max<(dimensions[i][0]*dimensions[i][1]):
                    cur=(dimensions[i][0]**2+dimensions[i][1]**2)
                    index=i
                    max=(dimensions[i][0]*dimensions[i][1])
        return(max)
            
        