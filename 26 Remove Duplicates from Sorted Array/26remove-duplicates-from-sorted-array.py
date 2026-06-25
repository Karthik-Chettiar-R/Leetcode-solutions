class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return nums
        curr=nums[0]
        c=1
        j=1
        for i in range(1,len(nums)):
            if curr==nums[i]:
                
                continue
            else :
                nums[j]=nums[i]
                j+=1
                curr=nums[i]
                c+=1
        return c
