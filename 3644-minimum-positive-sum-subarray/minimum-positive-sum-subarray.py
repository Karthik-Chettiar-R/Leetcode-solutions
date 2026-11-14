class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        
        prefix=[0]

        for i in range(len(nums)):
            prefix.append(prefix[-1]+nums[i])

        mi=float('inf')

        for ra in range(l,r+1):
            for i in range(len(nums)-ra+1):
                if prefix[i+ra]-prefix[i]>0:
                    mi=min(mi,prefix[i+ra]-prefix[i])

        if mi==float('inf'):
            return -1
        return mi


            


        
