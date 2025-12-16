class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0

        for i in range(len(nums)-2):
            c=1
            s=0
            for j in range(i,len(nums)):
                if c>=3:
                    count+=1
                if j==i:
                    s=nums[j]-nums[j+1]
                    c+=1

                elif j<len(nums)-1:
                    if nums[j]-nums[j+1]==s:
                        c+=1
                    else :
                        break
                    
        return count

        