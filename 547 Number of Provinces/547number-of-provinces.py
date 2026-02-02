



class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        visited=[False]*n
        def dfs(city):
            for neighbour in range(n):
                if isConnected[city][neighbour] and not visited[neighbour]:
                    visited[neighbour]=True
                    dfs(neighbour)
        c=0
        for i in range(n):
            if not visited[i]:
                c+=1
                dfs(i)
        return c
             
        


        