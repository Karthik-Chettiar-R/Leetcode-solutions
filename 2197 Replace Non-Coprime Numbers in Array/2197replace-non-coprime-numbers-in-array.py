from fractions import gcd
def lcm(num1,num2):
    return (num1*num2)//gcd(num1,num2)
class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<=1:
            return nums
        stack=[]
        stack.append(nums[0])
        for i in range(1,len(nums)):
            stack.append(nums[i])
            j=len(stack)-2
            while(gcd(stack[j],stack[j+1])>1 and j>=0):
              
                res=lcm(stack[j],stack[j+1])
                stack.pop()
                stack.pop()
                stack.append(res)
                j-=1
                
                    

        return stack

        