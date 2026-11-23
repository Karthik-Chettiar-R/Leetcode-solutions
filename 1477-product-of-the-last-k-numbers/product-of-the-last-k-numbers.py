class ProductOfNumbers(object):

    def __init__(self):
        self.queue=[1]
        self.product=1
        self.lastOccurenceOfZero=-1
    
    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num==0:
            self.product=1
            self.queue.append(self.product)
            self.lastOccurenceOfZero=len(self.queue)
            return

        
        self.queue.append(self.product*num)
        self.product*=num
        return
        


    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if len(self.queue)-k+1<=self.lastOccurenceOfZero:
            return 0

        #
        #return self.queue
        return self.queue[len(self.queue)-1]/self.queue[len(self.queue)-k-1]


        
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)