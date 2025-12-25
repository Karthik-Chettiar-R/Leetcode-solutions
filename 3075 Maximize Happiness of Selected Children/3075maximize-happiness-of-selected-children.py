class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort()
        c=0
        r=0
        for i in range(len(happiness)-1,len(happiness)-k-1,-1):
            
            if happiness[i]-c>0:
                r+=happiness[i]-c
            c+=1
        return r
         
        
        
        