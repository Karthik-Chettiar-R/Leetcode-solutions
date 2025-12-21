class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=str(n)
        s=s[::-1]
        si=int(s)
        return abs(si-n)