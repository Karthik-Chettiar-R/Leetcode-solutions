class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp=[[0]*len(grid[0]) for _ in range(len(grid))]

        dp[0][0]=grid[0][0]

        for i in range(1,len(grid[0])):
            dp[0][i]=grid[0][i]+dp[0][i-1]
        for i in range(1,len(grid)):
            dp[i][0]=grid[i][0]+dp[i-1][0]

        for i in range(1,len(grid[0])):
            for j in range(1,len(grid)):
                d=float('inf')
                r=float('inf')
                
                dp[j][i]=grid[j][i]+min(dp[j-1][i],dp[j][i-1])

        return dp[len(dp)-1][len(dp[0])-1]

