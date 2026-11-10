class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        dp=[0 for i in range(len(costs)+1)]

        for i in range(1,len(costs)+1):
            step1=float('inf')
            step2=float('inf')
            step3=float('inf')

            j0=i-1

            j=i

            i1=i-1
            i2=i-2
            i3=i-3

            step1=dp[i1]+costs[j0]+(j-i1)**2

            if i-2>-1:
                step2=min(dp[i2]+costs[j0]+(j-i2)**2,dp[i1]+costs[j0]+(j-i1)**2)

            if i-3>-1:
                step3=min(dp[i3]+costs[j0]+(j-i3)**2,dp[i2]+costs[j0]+(j-i2)**2,dp[i1]+costs[j0]+(j-i1)**2)

            dp[i]=min(step1,step2,step3)

        return dp[-1]



