from collections import deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        done=0
        degree=[0]*numCourses
        adj=[[] for _ in range(numCourses)]
        for i,j in prerequisites:
            adj[j].append(i)
            degree[i]+=1

        dq = deque([i for i in range(numCourses) if degree[i] == 0])

                
        
        while(dq):
            course=dq.popleft()
            done+=1
            for i in adj[course]:
                degree[i]-=1
                if degree[i]==0:
                    dq.append(i)
                    
        if done==numCourses:
            return True
        return False


        