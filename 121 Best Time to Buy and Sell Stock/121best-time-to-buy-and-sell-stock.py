class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min_price=float('inf')
        max_price=0
        for i in prices:
            min_price=min(min_price,i)
            max_price=max(max_price,i-min_price)
        return max_price