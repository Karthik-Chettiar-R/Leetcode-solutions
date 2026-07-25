class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def rec(num):
            max1=num%10
            num//=10
            max2=num%10

            if max1<max2:
                max1,max2=max2,max1

            num//=10

            while(num>0):
                if num%10>max1:
                    max2=max1
                    max1=num%10

                elif num%10>max2:
                    max2=num%10

                num//=10

            return max1*max2
                    


            
        return rec(n)