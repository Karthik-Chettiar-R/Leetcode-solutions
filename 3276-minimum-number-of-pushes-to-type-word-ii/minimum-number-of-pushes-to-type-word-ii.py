import heapq
class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """


        freq={}

        for i in range(len(word)):
            if word[i] not in freq:
                freq[word[i]]=1
            else:
                freq[word[i]]+=1
        
        sortedFrequency=sorted(freq.values(),key=lambda item:-item)

        
        pushes=0
        multiplier=1
        for i in range(len(sortedFrequency)):
            if i>7 and i<16:
                multiplier=2
            if i>15 and i<24:
                multiplier=3
            if i>23:
                multiplier=4

            pushes+=(sortedFrequency[i])*multiplier

        return pushes

        

                
        
