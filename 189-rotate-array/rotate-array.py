class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        left=nums[len(nums)-k:]
        right=nums[:len(nums)-k]

        i=0

        while(i<len(left)):
            nums[i]=left[i]
            i+=1

        j=0

        while(j<len(right)):
            nums[i]=right[j]
            j+=1
            i+=1


        