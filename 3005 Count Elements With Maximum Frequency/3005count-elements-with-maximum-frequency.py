class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            d[i]=nums.count(i)
        m=0
        r=0
        i=0
        for key in nums:
            if d[key]>m:
                m=d[key]
        for key in nums:
            if d[key]==m:
                r+=d[key]
                i+=1
                
        return i
                
            
            
        