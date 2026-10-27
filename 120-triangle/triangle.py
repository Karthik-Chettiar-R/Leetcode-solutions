import copy

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        triangleDP=copy.deepcopy(triangle)

        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                triangleDP[i][j] = float('inf')

        triangleDP[0][0]=triangle[0][0]
        

        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):

                left=0
                right=0

                if j-1 <0:
                    left=float('inf')
                else:
                    left=triangleDP[i-1][j-1]

                if j>=len(triangle[i-1]):
                    right=float('inf')

                else:

                    right=triangleDP[i-1][j]

                triangleDP[i][j]=triangle[i][j]+min(left,right)


        return min(triangleDP[len(triangle)-1])



        

        

        def minTriangle(top,level,triangle):
            i,j=top[0],top[1]

            if level==len(triangle)-1:
                return triangle[i][j]

            top_left_triangle=[i+1,j]

            top_right_triangle=[i+1,j+1]

            left_i=i+1
            left_j=j

            right_i=i+1
            right_j=j+1

            return min(triangle[i][j]+minTriangle(top_left_triangle,level+1,triangle),triangle[i][j]+minTriangle(top_right_triangle,level+1,triangle))





        