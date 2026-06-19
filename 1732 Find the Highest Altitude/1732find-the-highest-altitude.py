class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        currMax=0
        temp=0
        for i in range(len(gain)):
            temp+=gain[i]
            if temp>currMax:
                currMax=temp
        return currMax