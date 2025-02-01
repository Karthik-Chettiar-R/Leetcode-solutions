class Solution(object):
    def addBinary(self, a, b):
        
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if(len(a)>len(b)):
           b=b.zfill(len(a))
        else:
           a=a.zfill(len(b))
        end=len(a)
        end=end-1
        carry=0
        result=[]
        temp=0
        while(end!=-1):
            
            temp=(carry+int(a[end])+int(b[end]))%2
            result.append(str(temp))
            carry =(carry+int(a[end])+int(b[end]))//2
            end=end-1
        
        if carry==1:
            result.append("1")
        return ''.join(result[::-1])
