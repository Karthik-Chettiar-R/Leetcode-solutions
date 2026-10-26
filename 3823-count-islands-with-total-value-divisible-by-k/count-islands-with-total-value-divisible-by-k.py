class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """

        stack=[]

        toBeProcessed=set()

        noOfIslands=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    toBeProcessed.add((i,j))

        while(toBeProcessed):
            stack.append(toBeProcessed.pop())

            value=0

            while(stack):

                current=stack.pop()

                currentI,currentJ=current[0],current[1]

                value+=grid[currentI][currentJ]

                if currentI-1>-1 and (currentI-1,currentJ) in toBeProcessed:
                    stack.append((currentI-1,currentJ))
                    toBeProcessed.remove((currentI-1,currentJ))

                if currentJ-1>-1 and (currentI,currentJ-1) in toBeProcessed:
                    stack.append((currentI,currentJ-1))
                    toBeProcessed.remove((currentI,currentJ-1))

                if currentI+1<len(grid) and (currentI+1,currentJ) in toBeProcessed:
                    stack.append((currentI+1,currentJ))
                    toBeProcessed.remove((currentI+1,currentJ))

                if currentJ+1<len(grid[0]) and (currentI,currentJ+1) in toBeProcessed:
                    stack.append((currentI,currentJ+1))
                    toBeProcessed.remove((currentI,currentJ+1))

            if value%k==0:
                noOfIslands+=1

        return noOfIslands

                

            




        

        