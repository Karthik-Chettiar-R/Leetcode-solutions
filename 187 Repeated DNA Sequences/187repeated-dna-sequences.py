def hashCalculate(str):
    hashish=0
    expo=9
    for i in range(10):
        if str[i]=='A':
            hashish+=1*pow(10,expo)
            expo-=1
        elif str[i]=='C':
            hashish+=2*pow(10,expo)
            expo-=1
        elif str[i]=='G':
            hashish+=3*pow(10,expo)
            expo-=1
        elif str[i]=='T':
            hashish+=4*pow(10,expo)
            expo-=1

    return hashish

def indice(ch):
    if ch=='A':
        return 1
    elif ch=='C':
        return 2
    elif ch=='G':
        return 3
    elif ch=='T':
        return 4

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        retList=set()
        seen=set()

        i=1
        j=10

        if len(s)<10:
            return []

        Hashish=hashCalculate(s)
        seen.add(Hashish)

        while(j<len(s)):
            Hashish-=(indice(s[i-1])*1000000000)
            Hashish*=10
            Hashish+=indice(s[j])
            if Hashish in seen:
                
                retList.add(s[i:j+1])
                i+=1
                j+=1
                continue
            seen.add(Hashish)
            j+=1
            i+=1
        return list(retList)



        