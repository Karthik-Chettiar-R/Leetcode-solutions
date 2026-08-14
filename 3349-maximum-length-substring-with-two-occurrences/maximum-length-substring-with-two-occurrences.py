class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        

        freq={}
        m=0
        mTemp=0
        i=0
        j=0

        while(j<len(s)):
            if s[j] not in freq:
                freq[s[j]]=1
                
            else:
                freq[s[j]]+=1
            mTemp+=1
            
            
            if freq[s[j]]>2:
                while(freq[s[j]]>2):
                    freq[s[i]]-=1
                    i+=1
                    mTemp-=1
            
            m=max(m,mTemp)
            j+=1

        return m

        

