class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        maxFreq=1
        left=0
        windowSum=0
        for right in range(len(nums)):
            windowSum+=nums[right]
            while(nums[right]*(right-left+1)-windowSum >k):
                
                windowSum-=nums[left]
                left+=1
            maxFreq=max(maxFreq,right-left+1)
        return maxFreq
        

            



        