class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        dummyS=list(s)
        sL=list(s)
        gL=list(goal)
   
        i=0
        for i in range(len(s)):
            if sL==gL:
                return True
            for j in range(len(s)):
                sL[j]=dummyS[(j+i)%len(s)]
            
        if sL==gL:
            return True
        return False

            