def mover(i,j,m,n,grid,memo):
    if i==m and j==n:
        return 1
    elif i > m or j > n:
        return 0
    

    else :
        if (i,j) in memo :
            return memo[(i,j)] 
        else :
            if i+1<=m and not grid[i+1][j]:
                r=mover(i+1,j,m,n,grid,memo)
            else :
                r=0
            if j+1 <=n and not grid[i][j+1]:
                d=mover(i,j+1,m,n,grid,memo)
            else :
                d=0
            memo[(i,j)]=r+d
            return r+d



class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        memo={}
        if obstacleGrid[0][0]==1:
            return 0
        return mover(0,0,len(obstacleGrid)-1,len(obstacleGrid[0])-1,obstacleGrid,memo)
        