
def mover(i,j,fx,fy,memo):
    if (i,j) in memo:
        return memo[(i,j)]
    elif (i,j) not in memo:

        
        if i==fx and j==fy:
            return 1
        elif i>fx or j>fy:
            return 0
        else :
            r=mover(i+1,j,fx,fy,memo)+mover(i,j+1,fx,fy,memo)
            memo[(i,j)]=r
            return r
       
    

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int 
        :type n: int 
        :rtype: int 
        """
        memo={}
        return mover(1,1,m,n,memo)
        