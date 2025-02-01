class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        end=len(digits)-1
        while(end!=-1):
            if(digits[end]!=9):
                digits[end]=digits[end]+1
                return digits
            else:
                digits[end]=0
                end=end-1
        digits.insert(0,1)
        return digits