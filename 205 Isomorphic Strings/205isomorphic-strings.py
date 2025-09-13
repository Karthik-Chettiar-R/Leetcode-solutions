class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        ds={}
        dt={}
        dones=set()
        donet=set()
        

        for i in range(len(s)):
            if s[i] not in dones:
                ds[s[i]]=t[i]
                
                
                dones.add(s[i])
            
            else:
                if ds[s[i]]!=t[i]:
                    return False

            if t[i] not in donet:
                dt[t[i]]=s[i]
                donet.add(t[i])
            else:
                if dt[t[i]]!=s[i]:
                    return False
        return True
                    
                
        