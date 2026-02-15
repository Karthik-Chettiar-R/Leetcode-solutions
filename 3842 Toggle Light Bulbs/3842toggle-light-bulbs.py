class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        s=set()

        for i in bulbs:
            if i not in s:
                s.add(i)
            else :
                s.remove(i)

        r=list(s)
        r.sort()
        return r
        