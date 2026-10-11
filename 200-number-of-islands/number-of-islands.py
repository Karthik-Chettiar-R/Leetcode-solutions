class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        stack=[]
        done=set()
        count=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and (i,j) not in done:
                    stack.append((i,j))
                    done.add((i,j))

                    while(stack):
                        current=stack.pop()
                        currentI,currentJ=current[0],current[1]

                        if currentI-1>-1 and grid[currentI-1][currentJ]=='1' and (currentI-1,currentJ) not in done:
                            stack.append((currentI-1,currentJ))
                            done.add((currentI-1,currentJ))

                        if currentI+1<len(grid) and grid[currentI+1][currentJ]=='1' and (currentI+1,currentJ) not in done:
                            stack.append((currentI+1,currentJ))
                            done.add((currentI+1,currentJ))

                        if currentJ-1>-1 and grid[currentI][currentJ-1]=='1' and (currentI,currentJ-1) not in done:
                            stack.append((currentI,currentJ-1))
                            done.add((currentI,currentJ-1))

                        if currentJ+1<len(grid[0]) and grid[currentI][currentJ+1]=='1' and (currentI,currentJ+1) not in done:
                            stack.append((currentI,currentJ+1))
                            done.add((currentI,currentJ+1))

                    count+=1

        return count

                    

                        

                        