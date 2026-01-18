class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        v=0
        c=0
        vowel=set({"a","e","i","o","u"})
        for i in range(len(s)):
            if s[i] in vowel  :
                v+=1
            else:
                if s[i].isalpha():
                    c+=1
        if c>0:
            return v//c
        else:
            return 0
                
        