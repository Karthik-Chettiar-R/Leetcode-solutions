class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ma=-float('inf')

        maximum=[]

        minimum=[float('inf') for i in range(len(nums))]

        mi=float('inf')

        for i in range(len(nums)):
            if nums[i]>ma:
                ma=nums[i]

            maximum.append(ma)

        for i in range(len(nums)-1,-1,-1):
            if mi>nums[i]:
                mi=nums[i]

            minimum[i]=mi


        for i in range(len(nums)):
            if maximum[i]-minimum[i]<=k:
                return i

        return -1


        