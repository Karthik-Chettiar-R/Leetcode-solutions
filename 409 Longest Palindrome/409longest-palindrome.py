class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        frequency=[0]*58
        for i in range (len(s)):
            frequency[ord(s[i])-97]+=1

        odd=0
        ans=0

        for i in range(58):
            if not odd and frequency[i]%2==1:
                odd=1
                ans+=1
                
            if frequency[i]%2==0:
                ans+=frequency[i]
            if frequency[i]%2==1:
                ans+=frequency[i]-1

        return ans
            

            

            
                

        
    

        
        