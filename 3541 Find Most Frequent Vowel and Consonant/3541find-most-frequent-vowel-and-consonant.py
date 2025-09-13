class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        freqV=[0]*5
        
        freqC=[0]*26
        for i in range(len(s)):
            if s[i]=='a':
                freqV[0]+=1
            elif s[i]=='e':
                freqV[1]+=1
            elif s[i]=='i':
                freqV[2]+=1
            elif s[i]=='o':
                freqV[3]+=1
            elif s[i]=='u':
                freqV[4]+=1
            else:
                freqC[ord(s[i])-97]+=1

        return max(freqV)+max(freqC)

        
                

        

        
            
            
            
        