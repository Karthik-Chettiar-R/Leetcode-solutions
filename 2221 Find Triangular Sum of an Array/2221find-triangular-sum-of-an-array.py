class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1):
            newNums=[0]*(len(nums)-1)
            it=0
            j=1
            for k in range(len(nums)-1):
                newNums[k]=nums[it]+nums[j]
                it+=1
                j+=1

            nums=newNums
        r=nums[0]
        return r%10
                
                 

            
            
        
        