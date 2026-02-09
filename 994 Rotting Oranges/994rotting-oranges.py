class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue=[]
        fresh=set()
        done=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j))
                    done.add((i,j))
                if grid[i][j]==1:
                    fresh.add((i,j))
        t=0
        while(len(fresh)>0 and queue):
            q=[]
            for i in range(len(queue)):
                
                done.add((queue[i][0],queue[i][1]))
                if queue[i][0]-1>=0 and (queue[i][0]-1,queue[i][1]) in fresh:
                    q.append((queue[i][0]-1,queue[i][1]))
                    fresh.remove((queue[i][0]-1,queue[i][1]))
                if queue[i][1]-1>=0 and (queue[i][0],queue[i][1]-1) in fresh:
                    q.append((queue[i][0],queue[i][1]-1))
                    fresh.remove((queue[i][0],queue[i][1]-1))
                if queue[i][0]+1<=len(grid)-1 and (queue[i][0]+1,queue[i][1]) in fresh:
                    q.append((queue[i][0]+1,queue[i][1]))
                    fresh.remove((queue[i][0]+1,queue[i][1]))
                if queue[i][1]+1<=len(grid[0])-1 and (queue[i][0],queue[i][1]+1) in fresh:
                    q.append((queue[i][0],queue[i][1]+1))
                    fresh.remove((queue[i][0],queue[i][1]+1))
            t+=1
            queue=q
            q=[]
        if fresh:
            return -1
        return t

                
