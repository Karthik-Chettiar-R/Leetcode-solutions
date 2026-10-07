class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        parenthesis={'(',')'}

        stack=[]

        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])

            elif s[i]==')':

                if stack and stack[-1]=='(':
                    stack.pop()
                    score=1
                    stack.append(score)
    

                else:
                    score=stack.pop()
                    stack.pop()
                    stack.append(2*score)

            if len(stack)>1 and stack[-1] not in parenthesis and stack[-2] not in parenthesis:
                while(len(stack)>1 and stack[-2] not in parenthesis):
                    score1=stack.pop()
                    score2=stack.pop()
                    score=score1+score2
                    stack.append(score)


        return stack[-1]


            


                            



       
            