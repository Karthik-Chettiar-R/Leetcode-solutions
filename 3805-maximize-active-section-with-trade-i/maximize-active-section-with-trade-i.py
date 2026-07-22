class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s='1'+s
        s+='1'

        flag=1
        section="1"
        oneORzero=[]
        sections=[]

        for i in range(1,len(s)):
            if s[i] =='1':
                if flag==0:
                    flag=1
                    sections.append(section)
                    oneORzero.append(0)
                    section='1'
                else:
                    section+='1'
            elif s[i]=='0':
                if flag==1:
                    flag=0
                    sections.append(section)
                    oneORzero.append(1)
                    section='0'
                else:
                    section+='0'
        sections.append(section)
        oneORzero.append(1)
        size=0

        
        if len(sections)<5:
            
            size=0
            for i in range(len(sections)):
                if oneORzero[i]:
                    size+=len(sections[i])
                    if i==0:
                        size-=1
                    if i==len(sections)-1:
                        size-=1
            return size

        leftMost=0
        left=1
        middle=2
        right=3
        rightMost=4

        size=0
        for i in range(len(sections)):
            if oneORzero[i]:
                size+=len(sections[i])
                if i==0:
                    size-=1
                if i==len(sections)-1:
                    size-=1
        l=0
        r=4
        maxSize=size
        while(rightMost<len(sections)):
            currSize=len(sections[left])+len(sections[right])
            
            if size+currSize>maxSize:
                maxSize=currSize+size
                l=leftMost
                r=rightMost

            leftMost+=2
            left+=2
            middle+=2
            right+=2
            rightMost+=2
        
        active=0

        return maxSize
        for i in range(len(sections)):
            if i in range(l,r+1):
                active+=len(sections[i])
            else :
                if int(sections[i])>0:
                    active+=len(sections[i])

        

        return sections
        
        
        





        
                    
        