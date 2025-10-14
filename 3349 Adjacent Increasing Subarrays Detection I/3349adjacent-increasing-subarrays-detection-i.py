
def inc(arr,i,k):
    for j in range(k-1):
        if arr[i]<arr[i+1]:
            i+=1
            continue
        else:
            return False
    return True
    
    
        
        
class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        i=0
        if k==1:
            return True
        
        while(i<len(nums)):
            if i+k<=len(nums) and inc(nums,i,k) and i+k+k<=len(nums) and inc(nums,i+k,k):
                return True
            i+=1
        return False

        