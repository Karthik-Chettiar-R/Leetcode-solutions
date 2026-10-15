class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinctCount=[0]
        def subarray(nums,distinct,count,i,j):
            if j>=len(nums):
                return

            if nums[j] not in distinct:
                count+=1
                distinct.add(nums[j])
            distinctCount[0]+=count**2

            subarray(nums,distinct.copy(),count,i,j+1)

        distinct=set()
        for i in range(len(nums)):
            subarray(nums,distinct.copy(),0,i,i)

        return distinctCount[0]


