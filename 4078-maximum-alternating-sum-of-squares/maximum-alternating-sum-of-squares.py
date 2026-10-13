class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort(key=lambda x:abs(x))
        su=0
        half=len(nums)//2
        for i in range(len(nums)):
            if i<half:
                su-=nums[i]**2
            else:
                su+=nums[i]**2

        return su
            