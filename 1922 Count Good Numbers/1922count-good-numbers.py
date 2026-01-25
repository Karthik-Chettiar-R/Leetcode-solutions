def rec(n):
    mod=10**9+7
    odd=(n+1)//2
    even=n//2
    return (pow(5,odd,mod)*pow(4,even,mod))

class Solution():
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        return rec(n)%(10**9+7)


        