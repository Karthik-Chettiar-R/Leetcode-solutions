class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        elif len(nums)==3:
            return max(nums[0]+nums[2],nums[1])
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=nums[1]
        dp[2]=dp[0]+nums[2]

        for i in range(3,len(nums)):
            onestep=nums[i]+dp[i-2]
            twostep=nums[i]+dp[i-3]
            dp[i]=max(onestep,twostep)
        return max(dp[i],dp[i-1])



