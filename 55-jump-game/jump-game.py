class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp=[False for i in nums]

        jump=nums[0]-1

        for i in range(1,len(nums)):
            if jump<0:
                return False
            if nums[i]>jump:
                jump=nums[i]

            jump-=1

            

        

        return True

        












