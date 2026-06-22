from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        freq=Counter(text)


        x=min(freq['b'],freq['a'],freq['n'])
        y=min(freq['l'],freq['o'])//2
        return min(x,y)