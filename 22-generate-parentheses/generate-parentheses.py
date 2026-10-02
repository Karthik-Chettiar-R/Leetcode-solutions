def generate(result,parenthesis,n,count,leftCount,rightCount):
    if count==n*2:
        result.append(parenthesis)
        return
    if leftCount<=n:

        if leftCount>rightCount :
            generate(result,parenthesis+')',n,count+1,leftCount,rightCount+1)
            if leftCount<n:
                generate(result,parenthesis+'(',n,count+1,leftCount+1,rightCount)

        else:
            if leftCount<n:
                generate(result,parenthesis+'(',n,count+1,leftCount+1,rightCount)

    return

    

    

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result =[]

        generate(result,'',n,0,0,0)

        return result
         