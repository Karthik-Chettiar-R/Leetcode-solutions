class Solution(object):
    def earliestTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """

        min=1000
        for i in tasks:
            if (i[0]+i[1])<min:
                min=i[0]+i[1]
        return min
        