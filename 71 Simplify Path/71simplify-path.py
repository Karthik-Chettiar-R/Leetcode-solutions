class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        s=path.split('/')
        stack=[]
        for i in s:
            if i=='' or i=='.':
                continue
            else:
                if i=='..':
                    if stack:
                        stack.pop()
                else :
                    stack.append(i)
        ret='/'
        if not stack:
            return '/'

        else :
            for i in stack:
                ret+=i
                ret+='/'
        return ret[:len(ret)-1]

        