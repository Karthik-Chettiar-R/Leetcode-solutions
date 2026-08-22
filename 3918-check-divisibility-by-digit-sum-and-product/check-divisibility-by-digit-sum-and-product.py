def digitSum(n):
    s=0

    stringN=str(n)
    for i in range(len(str(stringN))):
        s+=int(stringN[i])

    return s

def digitProduct(n):
    s=1
    stringN=str(n)
    for i in range(len(str(stringN))):
        s*=int(stringN[i])

    return s

class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        

        return n%(digitSum(n)+digitProduct(n))==0