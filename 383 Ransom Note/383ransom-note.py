from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        freq1=Counter(ransomNote)
        freq2=Counter(magazine)

        for key in freq1:
            if key not in freq2:
                return False
            if freq1[key]>freq2[key]:
                return False
        return True