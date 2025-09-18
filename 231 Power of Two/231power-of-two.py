class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        s=format(n,'b')
        if s.count("1")>1:
            return False
        else:
            return True
        