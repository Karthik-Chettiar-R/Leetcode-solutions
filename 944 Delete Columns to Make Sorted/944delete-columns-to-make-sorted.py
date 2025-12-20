
    

class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        r=0
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if strs[j][i]<strs[j-1][i]:
                    r+=1
                    break
        
            
        return r
        