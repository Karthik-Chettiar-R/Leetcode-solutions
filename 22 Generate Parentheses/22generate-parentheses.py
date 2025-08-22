
def helper(i,n,parenthesis,left,right,ret):
    if right==n and left==n:
        ret.append(parenthesis)
        return

    if left ==right:
        helper(i+1,n,parenthesis+"(",left+1,right,ret)
    elif left==n and right <n:
        helper(i+1,n,parenthesis+")",left,right+1,ret)
    elif left>right:
        if (left<n):
            helper(i+1,n,parenthesis+"(",left+1,right,ret)
        helper(i+1,n,parenthesis+")",left,right+1,ret)
    

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret=[]
        helper(1,n,"",0,0,ret)
        return ret
        