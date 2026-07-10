class DSU:
    def __init__(self,nums):
        self.parent=[i for i in range(len(nums))]

    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])

        return self.parent[x]

    def union(self,x,y):
        rootX=self.find(x)
        rootY=self.find(y)

        if rootX==rootY:
            return False
        else:
            self.parent[rootY]=rootX
            return True

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """

        dsu=DSU(nums)

        i=1

        while(i<len(nums)):
            if abs(nums[i-1]-nums[i])<=maxDiff:
                dsu.union(i-1,i)
                i+=1
            else:
                i+=1

        output=[False for i in range(len(queries))]

        for i in range(len(queries)):
            if dsu.find(queries[i][0])==dsu.find(queries[i][1]):
                output[i]=True
            else:
                continue
        
        return output




        