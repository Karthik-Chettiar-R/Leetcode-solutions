class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x=0
        y=0
        xmin=len(grid[0])
        ymin=len(grid)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1 and j>x:
                    x=j

        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j]==1 and i>y:
                    y=i

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1 and j<xmin:
                    xmin=j

        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j]==1 and i<ymin:
                    ymin=i

        

        return (x-xmin+1)*(y-ymin+1)
        

        