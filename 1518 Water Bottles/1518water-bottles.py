class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        full=numBottles
        drank=0
        empty=0
        if numExchange>numBottles:
            return numBottles
        elif numExchange==numBottles:
            return numBottles+1
        while(full):
            if full==1 and empty<numExchange-1:
                return drank+1
            drank+=full 
            empty+=full 
            
            full=empty//numExchange
            empty-=full*numExchange
        return drank
            
        