class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        j=1
        c=1
        length=1
        seen=set()
        if len(s)==0:
            return 0
        seen.add(s[0])

        while(j<len(s)):
            if s[j] in seen:
                seen.discard(s[i])
                i+=1
                c-=1
                
            
            elif s[j] not in seen:
                seen.add(s[j])
                j+=1
                c+=1
                if c>length:
                    length=c
        return length



