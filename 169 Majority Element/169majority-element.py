def mooresVotingAlgo(nums):
    curr=nums[0]
    count=1
    for i in range(1,len(nums)):
        if count<=0:
            count=1
            curr=nums[i]
        if nums[i]==curr:
            count+=1
        else:
            count-=1
        if count<=0:
            count=1
            curr=nums[i]
    return curr


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 
        if len(nums)<3:
            return nums[0]
        return mooresVotingAlgo(nums)