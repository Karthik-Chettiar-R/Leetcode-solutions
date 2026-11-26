class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """

        turn=True
        pick=10

        while(n>0 and pick>0):
            if n-pick<0:
                return not turn
            
            n-=pick
            pick-=1
            turn =not turn

        return not turn


            

        