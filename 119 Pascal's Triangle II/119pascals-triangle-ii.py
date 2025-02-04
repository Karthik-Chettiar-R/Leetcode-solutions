class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        a=[1]
        prev=[1,1]
        if rowIndex==0:
            return a
        i=2
        
        rowIndex=rowIndex+1
        while(i<rowIndex):
            j=1
            curr=[0]*(i+1)
            curr[0],curr[i]=1,1
            
            while(j<i):
                curr[j]=prev[j]+prev[j-1]
                j=j+1
            i=i+1
            prev=curr
        return prev


        