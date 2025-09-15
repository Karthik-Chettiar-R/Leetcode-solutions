class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        
        sentence=text.split()
        
        count=len(sentence)
        for word in sentence:
            flag=0
            for letter in brokenLetters:
                if letter in word:
                    count-=1
                    flag=1
                    break
            if flag==1:
                continue
        return count
                    
            
            
            
            
        