class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        

        balls=[]

        for i in range(len(boxes)):
            if boxes[i]=='1':
                balls.append(i)

        ret=[0 for _ in boxes]

        for i in range(len(boxes)):
            for j in balls:
                
                ret[i]+=abs(i-j)

        return ret
