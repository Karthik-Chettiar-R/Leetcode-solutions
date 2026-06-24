class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        s1=set(edges[0])
        s2=set(edges[1])

        for i in s1:
            if i in s2 :
                return i