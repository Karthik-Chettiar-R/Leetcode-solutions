class Solution(object):
    def rotateElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        containsNN=[0]*len(nums)
        newL=[]

        for i in range(len(nums)):
            if nums[i]>=0:
                containsNN[i]=1
                newL.append(nums[i])
        copyL=list(newL)
        if not newL:
            return nums
        k%=len(copyL)
        
            
        for j in range(len(newL)):
            newL[(j-k)%(len(copyL))]=copyL[j]
        copyL=list(newL)
        j=0
        for i in range(len(nums)):
            if containsNN[i] :
                nums[i]=newL[j]
                j+=1
        return nums
                
        