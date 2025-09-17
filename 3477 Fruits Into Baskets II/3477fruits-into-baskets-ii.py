class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        count=len(fruits)
        placed=[False]*len(fruits)
        full=[False]*len(baskets)
        for i in range(len(fruits)):
            for j in range(len(fruits)):
                if not placed[i] and not full[j] and fruits[i]<=baskets[j]:
                    placed[i]=True
                    full[j]=True
                    count-=1
        return count
            
        