def helper(b,e,s):
        if s==e:
            return True
        if b==len(s):
            return True
        if s[b]==s[e]:
            return helper(b+1,e-1,s)
        else:
            return False
class Solution(object):

   
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=''.join([char for char in s if char.isalnum()])
        return helper(0,len(st)-1,st.lower())

        