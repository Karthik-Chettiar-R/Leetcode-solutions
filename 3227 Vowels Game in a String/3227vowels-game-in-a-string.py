class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        vowel=0
        for i in s:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                vowel+=1

        if vowel==0:
            return False
        if vowel%2==1:
            return True
        if vowel%2==0:
            return True
        
            
        
        