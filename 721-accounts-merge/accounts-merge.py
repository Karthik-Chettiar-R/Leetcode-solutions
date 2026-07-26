import heapq

class DRU:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        

    def find(self,x):

        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])

        return self.parent[x]

    def union(self,x,y):
        rootX=self.find(x)
        rootY=self.find(y)

        if rootX==rootY:
            return False

        self.parent[rootY]=rootX
        


        return True

        
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        n=len(accounts)

        dru=DRU(n)

        for i in range(len(accounts)):
            i_accounts=set(accounts[i][1:])
            
            for j in range(i+1,len(accounts)):
                
                j_accounts=set(accounts[j][1:])
                if i_accounts & j_accounts:
                    dru.union(j,i)


        done=[0 for i in range(len(accounts))]

        ret=[]

        for i in range(len(accounts)):
            if done[i]:
                continue
            done[i]=1

            account=set()
            
            parent=dru.find(i)

            for acc in accounts[i][1:]:
                account.add(acc)

            for j in range(i+1,len(accounts)):
                if done[j]:
                    continue
                if parent==dru.find(j):
                    done[j]=1
                    for acc in accounts[j][1:]:
                        account.add(acc)

            
            a=[accounts[i][0]]

            acc=list(account)

            heapq.heapify(acc)
            while acc:
                a.append(heapq.heappop(acc))

            ret.append(a)

        return ret

                




        