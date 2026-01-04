import math
def isFour(num):
    d=0
    r=0
    for i in range(1,int(math.sqrt(num))+1):

        if num%i==0:
            d+=1
            if i==num//i:
                r+=i

            else :
                r+=(num//i)+i
                d+=1
                
    if d==4:
        return r
    else :
        return 0





class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=0
        
        for j in range(len(nums)):
            r+=isFour(nums[j])
        return r

        