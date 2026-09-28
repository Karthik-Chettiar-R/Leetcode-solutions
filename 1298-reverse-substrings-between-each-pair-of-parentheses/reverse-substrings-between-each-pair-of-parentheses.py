class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        

        portal={}

        stack=[]

        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                if stack:
                    portal2=stack.pop()
                    portal[portal2]=i
                    portal[i]=portal2

        direction=1

        substring=''

        i=0

        l=0

        while(i>-1 and i<len(s) and l<len(s)):
            if s[i]=='(':
                i=portal[i]
                direction=-direction
                i+=direction

            elif s[i]==')':
                i=portal[i]
                direction=-direction
                i+=direction
            
            else:
                substring+=s[i]
                i+=direction
                l+=1

        return substring

        