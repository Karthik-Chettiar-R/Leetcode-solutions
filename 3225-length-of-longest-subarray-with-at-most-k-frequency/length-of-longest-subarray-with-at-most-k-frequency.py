class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        freq={}

        i=0
        j=0
        longestSubArray=0
        while(j<len(nums)):
            if nums[j] not in freq:
                freq[nums[j]]=1
                
            else:
                freq[nums[j]]+=1

            if freq[nums[j]]>k:

                while(freq[nums[j]]>k):
                    freq[nums[i]]-=1
                    i+=1
            longestSubArray=max((j-i+1),longestSubArray)


            j+=1


        return longestSubArray

            
            



        