class Solution(object):
    def dominantIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)-1
        c=0
        for i in range(len(nums)-1):
            sum=0
            for j in range(i+1,len(nums)):
                sum+=nums[j]

            if nums[i]>sum/n:
                c+=1
            n-=1
        return c