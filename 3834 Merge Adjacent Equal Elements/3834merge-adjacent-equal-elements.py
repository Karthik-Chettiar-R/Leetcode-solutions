class Solution(object):
    def mergeAdjacent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack=[]
        i=0
        while(i<len(nums)):
            
            if len(stack)==0:
                stack.append(nums[i])
                i+=1
            else:
            
                if len(stack)>=2:
                    if stack[-2]==stack[-1]:
                        stack[-2]=stack[-2]*2
                        stack.pop()
                        continue
                        
                
                if stack[-1]==nums[i]:
                    stack[-1]=nums[i]+stack[-1]
                    i+=1
                else :
                    stack.append(nums[i])
                    i+=1
        while(len(stack)>1 and stack[-1]==stack[-2]):
            stack[-2]*=2
            stack.pop()
            
        return stack
            
                    