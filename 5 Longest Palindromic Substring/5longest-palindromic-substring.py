class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        longestP=""

        for i in range(len(s)):
            for j in range(i,len(s)):
                p=s[i:j+1]
                if p ==p[::-1]:
                    if len(longestP)<len(s[i:j+1]):
                        longestP=s[i:j+1]
        return longestP

        