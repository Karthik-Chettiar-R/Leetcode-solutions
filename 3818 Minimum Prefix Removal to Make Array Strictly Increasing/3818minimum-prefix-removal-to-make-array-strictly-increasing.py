class Solution(object):
    def minimumPrefixLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        for i in range(len(nums)-1-1,-1,-1):
            if nums[i]<nums[i+1]:
                continue
            else:
                break

        if i==0 and nums[i]<nums[i+1]:
            return 0
        
        return i+1