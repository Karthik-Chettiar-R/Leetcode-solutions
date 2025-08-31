class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        res=[]

        for i in range(len(order)):
            if order[i] in friends:
                res.append(order[i])
        return res
        