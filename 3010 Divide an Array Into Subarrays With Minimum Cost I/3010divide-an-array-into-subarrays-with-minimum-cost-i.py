class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=nums[0]
        nums.pop(0)

        nums.sort()
        r+=nums[0]
        r+=nums[1]
        return r