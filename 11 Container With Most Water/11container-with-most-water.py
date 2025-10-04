class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max=0
        i=0
        j=len(height)-1
        while(i<j):
            if min(height[i],height[j])*abs(i-j)>max:
                max=min(height[i],height[j])*abs(i-j)
            if height[i]<=height[j]:
                i+=1
            elif height[j]<height[i]:
                j-=1
        return max

                                                                                                                                                                                                     




        

        