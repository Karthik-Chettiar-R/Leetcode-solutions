class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        f=0
        t=0       
        for i in range(len(bills)):
            if bills[i]==5:
                f+=1
            else :
                if bills[i]==10:
                    if f>0:
                        f-=1
                        t+=1
                    else :
                        return False
                elif bills[i]==20:
                    if f>0 and t>0 :
                        f-=1
                        t-=1
                    elif f>2:
                        f-=3
                    else :
                        return False
        return True



        



































