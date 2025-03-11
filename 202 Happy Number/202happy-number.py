class Solution(object):
    

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def square(n):
            sum=0
            while n> 0:
                s=n%10
                sum+=s*s
                n=n/10
                
            return sum
        saw=set()
        while n!=1 and n not in saw:
            saw.add(n)
            n=square(n)
        if n==1 :
            return True
        else :
            return False
            


        