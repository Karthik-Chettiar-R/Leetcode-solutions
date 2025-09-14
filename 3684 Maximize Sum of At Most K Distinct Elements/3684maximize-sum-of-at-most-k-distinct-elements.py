class Solution(object):
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        nums.sort()
        max=0
        count=k
        lastIndex=len(nums)-1
        done=set()
        retList=[]
        while(count>0):
            if lastIndex<0:
                break
            if nums[lastIndex] not in done:
                
                
                count-=1
                retList.append(nums[lastIndex])
                done.add(nums[lastIndex])
                lastIndex-=1
            else:
                lastIndex-=1
            
        
            
        return retList
            
            
        
        