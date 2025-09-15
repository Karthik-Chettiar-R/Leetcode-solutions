class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        number=False
        symbol=False
        sym=""

        r=""
        if len(s)>=1 and (not s[0].isdigit() and s[0]!="+" and s[0] !="-" and s[0]!=" ") :
            return 0

        if len(s)==1 and not s[0].isdigit():
            return 0

        if len(s)==0:
            return 0
        
            
        for letter in s:
            if letter==" " and number==False and symbol==False:
                continue
            elif letter==" " and (number==True or symbol==True):
                break
            
            if letter.isalpha() or letter==".":
                break
            #alphabet encountered

            if (letter=="+" or letter=="-") and symbol==False:
                sym=letter
                
                symbol=True

            elif (letter=="+" or letter=="-") and symbol==True:
                break

            if letter.isdigit():
                r+=letter
                symbol=True
                number=True

        if len(r)==0:
            return 0

        if len(r)>0:
            if sym=="+":
                return min(int(r),2**31-1)
            elif sym=="-":
                return max(-int(r),-(2**31))

        return min(int(r),(2**31-1))
                
            

       # return 0

        

        


        

            
        