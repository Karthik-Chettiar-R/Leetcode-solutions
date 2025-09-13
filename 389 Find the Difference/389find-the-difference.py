class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tl=list(t)
        sl=list(s)
        tl.sort()
        sl.sort()
        

        for i in range(len(sl)):
            if sl[i]!=tl[i]:
                return tl[i]

        return tl[len(tl)-1]
            
        
        
            
            
        