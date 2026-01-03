
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=str(x)
        r=''
        ri=0
        mi=-2**31
        ma=2**31-1
        if s[0]=='-':
            for i in range(len(s)-1,0,-1):
                r+=s[i]
            
            ri=-int(r)
            if ri<mi:
                return 0
        else:
            r=s[::-1]
            ri=int(r)
            if ri>ma:
                return 0
        return ri
        
            