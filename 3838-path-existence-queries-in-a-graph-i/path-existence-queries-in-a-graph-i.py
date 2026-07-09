class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """

        ret=[False for i in range(len(queries))]
        i=0
        groups=[]
        curr=set()
        while(i<len(nums)-1):
            
            if abs(nums[i]-nums[i+1])<=maxDiff:
                curr.add(i)
                curr.add(i+1)
                i+=1
            else:
                if curr:

                    groups.append(curr)
                curr=set()
                i+=1
        if curr:
            groups.append(curr)

        

        for j in range(len(queries)):
            if queries[j][0]==queries[j][1]:
                ret[j]=True
                continue
            for s in groups:
                if queries[j][0] in s and queries[j][1] in s:
                    ret[j]=True
                    break
            
        
        return ret
            
                

            

        