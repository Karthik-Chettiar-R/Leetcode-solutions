class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """

        servers=[0 for i in queries]

        inter=[]

        for i in range(len(queries)):
            inter.append([queries[i],i])

        inter.sort(key = lambda x:x[0])
        
        logs.sort(key=lambda x:x[1])
        i=0
        j=0
        count=0
        done={}
        
        for it in range(len(inter)):

            newRight=inter[it][0]
            newLeft=newRight-x
            index=inter[it][1]

            while(j<len(logs) and logs[j][1]<=newRight):
                if logs[j][0] not in done:
                    done[logs[j][0]]=1
                else:
                    done[logs[j][0]]+=1
                j+=1

            while(i<len(logs) and i<=j and logs[i][1]<newLeft):
                if done[logs[i][0]]<=1:
                    done.pop(logs[i][0],None)

                else:
                    done[logs[i][0]]-=1
                i+=1

        

            servers[index]=n-len(done)

        return servers




