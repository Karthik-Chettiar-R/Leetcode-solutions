
mod=1000000007
class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        
        prefix=[0 for i in range(len(s)+1)]
        prefixSum=[0 for i in range(len(s)+1)]
        nonZero=[0 for i in range(len(s)+1)]
        powerOf10=[1 for i in range(len(s)+1)]

        for i in range(1,len(s)+1):
            powerOf10[i]=(powerOf10[i-1]*10)%mod
        
        summ=0
        currZero=0

        for i in range(len(s)):

            if s[i]!='0':
                summ+=int(s[i])

                prefix[i+1]=(prefix[i]*10+int(s[i]))%mod
                nonZero[i+1]=nonZero[i]+1

            else :
                prefix[i+1]=(prefix[i])%mod
                nonZero[i+1]=nonZero[i]

            prefixSum[i+1]=summ

            
        if len(s)==1:
            return [int(s[0])*int(s[0])]    
        
        ret=[0 for i in range(len(queries))]
        
        for i in range(len(queries)):
            summ=prefixSum[queries[i][1]+1]-prefixSum[queries[i][0]]

            power=nonZero[queries[i][1]+1]-nonZero[queries[i][0]]

            num=(prefix[queries[i][1]+1]-prefix[queries[i][0]]*powerOf10[power])%mod


            ret[i]=(summ*num)%(mod)

        return ret




























