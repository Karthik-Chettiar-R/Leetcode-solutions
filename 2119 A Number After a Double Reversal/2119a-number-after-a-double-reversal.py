class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """

        
        
        if num==int(str(int(str(num)[::-1]))[::-1]):
            return True
        else :
            return False