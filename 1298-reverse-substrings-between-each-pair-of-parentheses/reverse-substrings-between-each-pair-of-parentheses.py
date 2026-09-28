class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack=[]
        subString=''

        left=-1
        right=len(s)

        for i in range(len(s)):
            if s[i]=='(':
                left=i
                break

        for j in range(len(s)-1,-1,-1):
            if s[j]==')':
                right=j
                break

        if left==-1 or right==len(s):
            return s

        parenthesis=0

        for i in range(left,right+1):
            if s[i]=='(':
                stack.append(s[i])
                parenthesis+=1

            elif s[i]==')':
                if parenthesis<1:
                    if stack:
                        stack[-1]+=s[i]
                    else:
                        stack.append(s[i])

                    continue

                sub=stack.pop()

                if sub=='(':
                    parenthesis-=1
                    continue

                sub=sub[::-1]

                stack.pop()

                if stack and stack[-1]!='(':
                    stack[-1]+=sub
                else:
                    stack.append(sub)

           

            else:
                if not stack:
                    stack.append(s[i])
                else:
                    if stack[-1]=='(':
                        stack.append(s[i])
                    else:
                        stack[-1]+=s[i]
        
        if stack:
            return s[:left]+stack[-1]+s[right+1:]

        return s[:left]+s[right+1:]



       
       


