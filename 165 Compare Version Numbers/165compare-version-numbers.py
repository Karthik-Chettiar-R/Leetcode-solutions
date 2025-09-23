class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if version1.count(".")>=version2.count("."):
            for i in range(version1.count(".")-version2.count(".")):
                version2+=".0"
        else:
            for i in range(version2.count(".")-version1.count(".")):
                version1+=".0"

        if version1==version2:
            return 0

        l1=[]
        l2=[]
        str1=""
        str2=""
        
        


        for i in range(len(version1)):
            
            if version1[i]==".":
                l1.append(int(str1))
                str1=""
            else:
                str1+=version1[i]

        for i in range(len(version2)):
            
            if version2[i]==".":
                l2.append(int(str2))
                str2=""
            else:
                str2+=version2[i]
        l1.append(int(str1))
        l2.append(int(str2))

        for i in range(len(l1)):
            if l1[i]>l2[i]:
                return 1
            elif l2[i]>l1[i]:
                return -1
        return 0

    


        
                
            
            

    
                
    
        