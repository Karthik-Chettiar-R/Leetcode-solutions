class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]>len(nums) or nums[i]<0:
                nums[i]=0
        if len(nums)==1:
            if nums[0]==1:
                return 2
            else:
                return 1
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            if isinstance(nums[i],int):
                if isinstance(nums[nums[i]-1],int):
                    nums[nums[i]-1]='a'+str(nums[nums[i]-1])
                    continue
            else :
                if isinstance(nums[i],str):
                    if isinstance(nums[int(nums[i][1:])-1],int):
                        nums[int(nums[i][1:])-1]='a'+str(nums[int(nums[i][1:])-1])
        
        n=0
        for i in range(len(nums)):
            if isinstance(nums[i],int):
                n=i+1
                break
        if n:
            return n
        else :
            return len(nums)+1
        
