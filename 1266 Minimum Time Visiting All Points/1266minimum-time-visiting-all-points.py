def mover(i,j,l):
    t=0
    for k in range(len(l)):
        
        while([i,j]!=l[k]):
            if i>l[k][0]:
                if j>l[k][1]:
                    i-=1
                    j-=1
                    t+=1
                elif j==l[k][1]:
                    i-=1
                    t+=1
                elif j<l[k][1]:
                    i-=1
                    j+=1
                    t+=1
            elif i<l[k][0]:
                if j>l[k][1]:
                    i+=1
                    j-=1
                    t+=1
                elif j==l[k][1]:
                    i+=1
                    t+=1
                elif j<l[k][1]:
                    i+=1
                    j+=1
                    t+=1
            elif i==l[k][0]:
                if j>l[k][1]:
                    
                    j-=1
                    t+=1
                
                elif j<l[k][1]:
                    
                    j+=1
                    t+=1
    return t

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        return mover(points[0][0],points[0][1],points)