class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        stack=[]
        noOfCloseIslands=0
        toBeProcessed=set()

        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]==0:
                    toBeProcessed.add((i,j))
    
        while(toBeProcessed):  
            flag=0        
            if not stack:
                stack.append(toBeProcessed.pop())

            
            
            while(stack):
                current=stack.pop()
                currentI,currentJ=current[0],current[1]

                if currentI in {0,len(grid)-1} or currentJ in {0,len(grid[0])-1}:
                    flag=1
 
                if currentI-1>-1 and (currentI-1,currentJ) in toBeProcessed and grid[currentI-1][currentJ] ==0:
                    
                    stack.append((currentI-1,currentJ))
                    toBeProcessed.remove((currentI-1,currentJ))
                    if currentI-1==0:
                        flag=1

                if currentJ-1>-1 and (currentI,currentJ-1) in toBeProcessed and grid[currentI][currentJ-1] ==0:
                    
                        
                    stack.append((currentI,currentJ-1))
                    toBeProcessed.remove((currentI,currentJ-1))
                    if currentJ-1==0:
                        flag=1

                if currentI+1<len(grid) and (currentI+1,currentJ) in toBeProcessed and grid[currentI+1][currentJ] ==0:
                    
                        
                    stack.append((currentI+1,currentJ))
                    toBeProcessed.remove((currentI+1,currentJ))
                    if currentI+1==len(grid)-1:
                        flag=1

                if currentJ+1<len(grid[0]) and (currentI,currentJ+1) in toBeProcessed and grid[currentI][currentJ+1] ==0:
                    stack.append((currentI,currentJ+1))
                    toBeProcessed.remove((currentI,currentJ+1))

                    if currentJ+1==len(grid[0])-1:
                        flag=1

            if flag==0:
                noOfCloseIslands+=1
                

            



        return noOfCloseIslands

                