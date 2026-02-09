class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        queue=[]
        queue.append((sr,sc))
        c=image[sr][sc]
        image[sr][sc]=color
        flag=0
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j]!=color:
                    flag=1
        if flag==0:
            return image
        done=set()
        done.add((sr,sc))
        while(queue):
            q=[]
            for i in range(len(queue)):
                if queue[i][0]-1>=0 and image[queue[i][0]-1][queue[i][1]]==c and (queue[i][0]-1,queue[i][1]) not in done:
                    q.append((queue[i][0]-1,queue[i][1]))
                    image[queue[i][0]-1][queue[i][1]]=color
                    done.add((queue[i][0]-1,queue[i][1]))
                if queue[i][1]-1>=0 and image[queue[i][0]][queue[i][1]-1]==c and (queue[i][0],queue[i][1]-1) not in done:
                    q.append((queue[i][0],queue[i][1]-1))
                    image[queue[i][0]][queue[i][1]-1]=color
                    done.add((queue[i][0],queue[i][1]-1))
                if queue[i][0]+1<len(image) and image[queue[i][0]+1][queue[i][1]]==c and (queue[i][0]+1,queue[i][1]) not in done:
                    q.append((queue[i][0]+1,queue[i][1]))
                    image[queue[i][0]+1][queue[i][1]]=color
                    done.add((queue[i][0]+1,queue[i][1]))
                if queue[i][1]+1<len(image[0]) and image[queue[i][0]][queue[i][1]+1]==c and (queue[i][0],queue[i][1]+1) not in done:
                    q.append((queue[i][0],queue[i][1]+1))
                    image[queue[i][0]][queue[i][1]+1]=color
                    done.add((queue[i][0],queue[i][1]+1))
            queue=q
        return image


            
        