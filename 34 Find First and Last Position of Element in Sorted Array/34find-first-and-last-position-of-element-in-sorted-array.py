class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s=set(nums)
        if target not in s:
            return [-1,-1]
        if len(nums)==1:
            return [0,0]
        i=0
        j=len(nums)-1
        while(i<=j):
            mid=(i+j)//2
            if nums[mid]==target:
                break
            else :
                if target>nums[mid]:
                    i=mid+1
                else :
                    j=mid-1
        mid=(i+j)//2
        i=mid
        
        while(i>-1 and nums[i]==target):
            i-=1
            
        j=mid+1
        while(j<len(nums) and nums[j]==target):
            j+=1
     
        return [i+1,j-1]    

