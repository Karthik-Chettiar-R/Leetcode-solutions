class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i=0
        j=0
        length=0
        c=0
        flip=0
        if len(nums)==0:
            return 0
        while(j<len(nums)):
            if nums[j]==0 and flip<k:
                flip+=1
                j+=1
                c+=1
                if length<c:
                    length=c
            elif nums[j]==0 and flip>=k:
                if nums[i]==0:
                    flip-=1
                    i+=1
                    c-=1
                elif nums[i]==1:
                    i+=1
                    c-=1
            else :
                j+=1
                c+=1
                if length<c:
                    length=c
        return length



        