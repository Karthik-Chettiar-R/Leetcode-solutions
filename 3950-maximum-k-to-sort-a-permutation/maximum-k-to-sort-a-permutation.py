class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        elementsNeedingSwaps=[]

        for i,num in enumerate(nums):
            if num!=i:
                elementsNeedingSwaps.append(num)

        

        if not elementsNeedingSwaps:
            return 0

        anded=elementsNeedingSwaps[0] & elementsNeedingSwaps[1]

        for i in range(2,len(elementsNeedingSwaps)):
            anded = anded & elementsNeedingSwaps[i]

        return anded

        