class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minStack=[]
        self.counter=0
        
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.counter==0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.minStack[-1],val))
        self.counter+=1


        

    def pop(self):
        """
        :rtype: None
        """
        self.minStack.pop()
        self.stack.pop()
        self.counter-=1

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()