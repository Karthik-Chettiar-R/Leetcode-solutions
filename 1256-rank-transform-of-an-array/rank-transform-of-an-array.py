class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        indexes={}

        rank=sorted(arr)

        ranks=[0 for i in range(len(arr))]

        
        currentRank=1
        for i in range(len(rank)):
            if rank[i] not in indexes:
                indexes[rank[i]]=currentRank
                currentRank+=1
        
        for i in range(len(arr)):
            ranks[i]=indexes[arr[i]]

        return ranks
            
            

        