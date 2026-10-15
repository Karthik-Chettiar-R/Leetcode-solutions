class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """

        
        goodInteger=''

        


        
        if num<len(str(sum)):
            return ""

        for i in range(sum//9):
            goodInteger+='9'

        if sum%9:
            goodInteger+=str(sum%9)

        

        for i in range(len(goodInteger),num):
            goodInteger+='0'


        if len(goodInteger)>num or len(goodInteger)<num:
            return ""
        return goodInteger


        



            

        