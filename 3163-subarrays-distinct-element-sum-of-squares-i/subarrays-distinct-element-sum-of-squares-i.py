class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        distinct=set()
        distinctCount=0
      

        for i in range(len(nums)):
            count=0
            distinct=set()

            for j in range(i,len(nums)):
                if nums[j] not in distinct:
                    count+=1
                    distinct.add(nums[j])

                distinctCount+=count**2
                

        return distinctCount

            



                



        