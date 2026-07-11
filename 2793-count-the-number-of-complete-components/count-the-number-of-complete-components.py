class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        graph=[[0 for i in range(n)] for i in range(n)]
        for i in range(len(graph)):
            graph[i][i]=1
        for i  in range(len(edges)):
            graph[edges[i][0]][edges[i][1]]=1
            graph[edges[i][1]][edges[i][0]]=1
            

        connectedComponents=0

        done=set()

        for i in range(len(graph)):
            connected=set()
            connected.add(i)
            flag=0
            queue=[]
            

            if i in done:
                continue
            done.add(i)
            for j in range(len(graph[i])):
                if graph[i][j]:
                    connected.add(j)
                    queue.append(j)
                    done.add(j)

            if len(connected)==1:
                connectedComponents+=1
                continue

            for j in queue:
                for k in range(len(graph[j])):
                    if graph[j][k] :
                        if k not in connected :
                            flag=1
                            break
                        
                    elif k in connected:
                        if not graph[j][k]:
                            flag=1
                            break
                if flag==1:
                    break

            
            if flag==0:
                connectedComponents+=1
        return connectedComponents




            




            

        