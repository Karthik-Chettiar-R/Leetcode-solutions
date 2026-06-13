class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        st=""
        wt=[]
        for i in range(len(words)):
            weight=0
            for j in range(len(words[i])):
                weight+=weights[ord(words[i][j])-97]
            
            ch=(-weight)%26
            wt.append(ch)
            ch+=96
            if ch==96:
                st+='z'
            else :
                st+=chr(ch)
            
        return st
