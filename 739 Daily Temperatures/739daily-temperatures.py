class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack=[]
        r=[0]*len(temperatures)
        for i in range(len(temperatures)):
            if len(stack)==0 :
                stack.append(i)
            else :
                if temperatures[stack[-1]]>=temperatures[i]:
                    stack.append(i)
                else:
                    while(len(stack)> 0 and temperatures[stack[-1]]<temperatures[i]):
                        r[stack[-1]]=i-stack[-1]
                        stack.pop()
                    stack.append(i)

        return r 