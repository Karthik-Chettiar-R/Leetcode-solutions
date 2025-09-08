def modul(number):
        while number>0:
            if number%10==0:
                return 0
            else:
                number//=10
        return 1
class Solution(object):
    
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1,n):
            if modul(i):
                if modul(n-i):
                    p=[i,n-i]
                    
                
                    return p
            
                

        
                
                
            
        