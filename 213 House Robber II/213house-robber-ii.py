class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0

        if len(nums)==1:
            return nums[0]

        if len(nums)==2:
            return max(nums[0],nums[1])

        if len(nums)==3:
            return max(nums[2],max(nums[0],nums[1]))

        dp1=[0]*(len(nums)-1)
        dp2=[0]*(len(nums)-1)
        dp1[0]=nums[0]
        dp1[1]=nums[1]
        dp1[2]=nums[0]+nums[2]

        for i in range(3 ,len(nums)-1):
            dp1[i]=nums[i]+max(dp1[i-2],dp1[i-3])

        dp2[0]=nums[1]
        dp2[1]=nums[2]
        dp2[2]=nums[3]+nums[1]

        for i in range(4,len(nums)):
            dp2[i-1]=nums[i]+max(dp2[i-3],dp2[i-4])
        return max(max(dp1),max(dp2))

        

        