class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        dp=[[set() for i in grid[0]] for i in grid]

        dp[0][0].add(grid[0][0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    continue
                
                total=set()
                if i-1>=0:
                    left=dp[i-1][j]

                    for item in left:
                        total.add(item ^ grid[i][j])

                if j-1>=0:
                    top=dp[i][j-1]

                    for item in top:
                        total.add(item ^ grid[i][j])

                dp[i][j]=total


                    

        
        return min(dp[-1][-1])

        
        def recursion(currentXOR,x,y,grid):
            if x+1>=len(grid):
                if y+1>=len(grid[0]):
                    return currentXOR

                return recursion(currentXOR ^ grid[x][y+1],x,y+1,grid)

            if y+1>=len(grid[0]):
                
                    return recursion(currentXOR ^ grid[x+1][y],x+1,y,grid)

            return min(recursion(currentXOR ^ grid[x][y+1],x,y+1,grid),recursion(currentXOR ^ grid[x+1][y],x+1,y,grid))

        