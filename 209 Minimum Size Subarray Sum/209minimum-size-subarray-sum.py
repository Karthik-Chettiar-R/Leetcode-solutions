class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        total=nums[0]
        i=0
        j=0
        minimum=float('inf')
        while(j<len(nums)):
            
            if total>=target:
                while(total>=target):
                    if j-i+1<minimum:
                        minimum=j-i+1
                    total-=nums[i]
                    i+=1
                    
            else:
                j+=1
                if j<len(nums):
                    total+=nums[j]

                

        if minimum==float('inf'):
            return 0
        return minimum
                

        