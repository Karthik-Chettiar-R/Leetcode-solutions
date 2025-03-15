class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        length=len(columnTitle)
        result=0
        lenS=0
        for i in range(length-1,-1,-1):
            

            result+=(ord(columnTitle[lenS])-64)*26**i
            lenS+=1
        return result

        