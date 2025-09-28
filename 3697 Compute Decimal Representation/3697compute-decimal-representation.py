class Solution(object):
    def decimalRepresentation(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        s=str(n)
        r=[]
        for i in range(len(s)):
            if int(s[i])*(10**(len(s)-i-1))==0:
                continue
                
            r.append(int(s[i])*(10**(len(s)-i-1)))
        return r