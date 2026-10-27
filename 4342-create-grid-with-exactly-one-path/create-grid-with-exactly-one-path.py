class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """

        grid=[[0 for _ in range(n)] for _ in range(m)  ]

        for i in range(m):
            grid[i][0]='.'

        for i in range(n):
            grid[m-1][i]='.'

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    grid[i][j]='#'

        for i in range(len(grid)):
            g=""
            for j in range(len(grid[i])):
                g+=grid[i][j]
            grid[i]=g


        return grid