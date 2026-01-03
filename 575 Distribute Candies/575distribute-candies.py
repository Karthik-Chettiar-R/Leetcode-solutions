class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        
        
        
        
        
        if len(candyType)//2<len(list(set(candyType))):
            return len(candyType)//2
        else :
            return len(list(set(candyType)))
        