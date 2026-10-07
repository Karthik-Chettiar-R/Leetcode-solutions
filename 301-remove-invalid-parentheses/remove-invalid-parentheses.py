from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        parenthesis={'(',')'}
        visited=set()
        output=[]
        s_length=len(s)

        def valid(s):

            stack=[]

            for i in range(len(s)):
                if s[i]=='(':
                    stack.append(s[i])

                elif s[i]==')':
                    if stack and stack[-1]=='(':
                        stack.pop()

                    else:
                        return False
                

            if stack:
                return False

            return True


        def bfs(s):

            queue=deque()
            minHeight=s_length

            queue.append(s)

            while(queue):

                currentString=queue.popleft()
                
                
                

                if len(currentString)<s_length-minHeight:
                    break

                if valid(currentString):
                    minHeight=s_length-len(currentString)
                    output.append(currentString)

                for i in range(len(currentString)):
                    if currentString[i] not in parenthesis:
                        continue
                    candidate=currentString[:i]+currentString[i+1:]
                    if candidate in visited:
                        continue
                    visited.add(candidate)
                    queue.append(candidate)

            return True

        bfs(s)
        
        return output




                

                





        
             