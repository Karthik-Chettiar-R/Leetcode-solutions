class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        it=len(s)
        jt=-1

        for i in range(len(s)):
            if s[i]=='b':
                it=i
                break

        for j in range(len(s)-1,-1,-1):
            if s[j]=='a':
                jt=j
                break

        if it>jt:
            return True

        return False

        

        

        