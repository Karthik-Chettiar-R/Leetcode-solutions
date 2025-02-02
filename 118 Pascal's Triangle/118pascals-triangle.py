class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return None
        a=[1]
        b=[]
        b.append(a)
        c=[[1],[1,1]]
        
        if numRows==1:
            return b
        if numRows==2:
            return c
        prev=[1,1]
        i=3
        while(i<=numRows):
            each=[0]*i
            each[0],each[i-1]=1,1
            j=1
            while(j+1<i):
                each[j]=prev[j]+prev[j-1]
                j=j+1
            prev=each
            c.append(each)
            i=i+1
        return c
        


        