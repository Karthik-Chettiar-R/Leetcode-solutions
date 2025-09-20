class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=format(n,'b')
        c=s.count("3")
        if n<=0:
            return False
        while(True):
            if n ==1:
                return True
            elif n%3!=0:
                return False
            
                
            else:
                n=n//3
        
        