class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """

        s=str(n)

        ss=0
        ds=0
        for i in range(len(s)):
            ss+=int(s[i])*int(s[i])
            ds+=int(s[i])
        if ss-ds>=50:
            return True
        else :
            return False









            
        