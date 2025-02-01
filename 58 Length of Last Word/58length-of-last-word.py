class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        counter=0
        for i in s:
            counter=counter+1
            if i==' ':
                counter=0
        return counter
