# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """



class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList=nestedList

        self.res=[]
        #self.recursion(self.nestedList,self.res)

        for i in range(len(self.nestedList)):
            self.recursion(self.nestedList[i],self.res)
        self.i=0

    def recursion(self,nestedList,res):
        if nestedList.isInteger():
            res.append(nestedList.getInteger())
            return 

        listNestedList=nestedList.getList()

        for i in range(len(listNestedList)):
            self.recursion(listNestedList[i],res)
    
    def next(self):
        """
        :rtype: int
        """

        it=self.i
        self.i+=1

        return self.res[it]
        

    def hasNext(self):
        """
        :rtype: bool
        """

        if self.i<len(self.res):
            return True

        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())