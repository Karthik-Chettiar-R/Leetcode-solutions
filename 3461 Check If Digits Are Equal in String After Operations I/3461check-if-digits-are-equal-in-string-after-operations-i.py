class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while(len(s)>2):
            i=1
            j=0
            newStr=""
            while(i<len(s)):
                
                newStr+=str((int(s[j])+int(s[j+1]))%10)
            
                 
                i+=1
                j+=1
            s=newStr
        if s[0]==s[1]:
            return True
        else :
            return False
        
    
                
                
        