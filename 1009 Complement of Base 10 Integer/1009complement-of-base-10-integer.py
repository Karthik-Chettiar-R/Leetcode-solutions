def bCompI(n):
    r=''
    while(n>1):
        if n%2==0:
            r+='0'
        else :
            r+='1'
        n//=2
        if n==1:
            r+='1'
    s=r[::-1]
    r=''
    for i in range(len(s)):
        if s[i]=='1':
            r+='0'
        else :
            r+='1'
    s=r[::-1]
    t=0
    it=1
    for i in range(1,len(s)):
        
        if s[i]=='0':
            it*=2
        else :
            it*=2
            t+=it
    if s[0]=='0':
        j=0
    else :
        t+=1
    return t



class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        elif n==1:
            return 0
        return bCompI(n)

    

        