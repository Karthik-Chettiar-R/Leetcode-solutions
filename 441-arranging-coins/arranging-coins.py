class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        step=1
        counter=0
        while(n>=step):
            if n-step>=0:
                counter+=1
                n-=step
                step+=1
        return counter

        