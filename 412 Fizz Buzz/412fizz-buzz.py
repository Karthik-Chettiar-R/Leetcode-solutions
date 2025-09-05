class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        str1=[]
        
        
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                str1.append("FizzBuzz")
            elif i%3==0 and i%5!=0:
                str1.append("Fizz")
            elif i%3!=0 and i%5==0:
                str1.append("Buzz")
            else:
                app=str(i)
                str1.append(app)
        return str1
                
                
            
            
            
            
        