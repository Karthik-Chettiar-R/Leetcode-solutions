class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        l=[int(operations[0])]
        j=0
        
        for i in range(1,len(operations)):
            if operations[i]=="C":
                l.pop()
                j-=1
            elif operations[i]=="+":
                l.append((l[j-1]+l[j]))
                j+=1

            elif operations[i]=="D":
                l.append((l[j]*2))
                j+=1
            else:
                l.append(int(operations[i]))
                j+=1
        sum=0
        for i in l:
            sum+=i
        return sum
            
            
        