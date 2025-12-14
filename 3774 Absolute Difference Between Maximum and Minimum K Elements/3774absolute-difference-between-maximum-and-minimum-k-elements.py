class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        s=0
        l=0
        for i in range(0,k):
            s+=nums[i]
        for j in range(len(nums)-k,len(nums)):
            l+=nums[j]
        return abs(s-l)
        