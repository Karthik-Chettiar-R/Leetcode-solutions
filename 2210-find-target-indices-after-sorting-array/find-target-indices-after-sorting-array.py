class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        count=0
        index=0
        retList=[]

        if target not in nums:
            return []

        for i in range(len(nums)):
            if nums[i]==target:
                count+=1

            elif nums[i]<target:
                index+=1

        retList.append(index)
        for i in range(count-1):
            retList.append(retList[-1]+1)

        return retList


        