class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        minDiff=float('inf')
        summation=0
        nums.sort()
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while(j<k and j<len(nums)-1 and k<=len(nums)-1):

                diff=abs(nums[i]+nums[j]+nums[k]-target)
                if diff<minDiff:
                    minDiff=diff
                    summation=nums[i]+nums[j]+nums[k]
                if nums[i]+nums[j]+nums[k]>target:
                    if k-1>j:
                        k-=1
                    else :
                        break
                else :
                    if j+1<k:
                        j+=1
                    else :
                        break
        return summation





