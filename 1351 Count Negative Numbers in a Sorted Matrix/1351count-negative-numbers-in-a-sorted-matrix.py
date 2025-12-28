class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        c=0
        j=0
        i=0
        j=len(grid)-1
        while(j>-1):
            if grid[j][i]<0:
                c+=(len(grid[0])-i)
                j-=1
            else :
                if i<len(grid[0])-1:
                    i+=1
                elif i==len(grid[0])-1 :
                    return c
        return c
                

                    
                    
            
        