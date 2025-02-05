class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy =0
        sell=0
        profit=0
        minp=float('inf')
        maxp=0
        for price in range(1,len(prices)):
            if buy==0 and prices[price-1]<prices[price]:
                minp=min(minp,prices[price-1])
                buy=1
            if buy ==1 and prices[price]<prices[price-1] :
                maxp=max(maxp,prices[price-1])
                buy=0
                profit+=maxp-minp
                maxp=0
                minp=float('inf')
            if buy==1 and price==len(prices)-1:
                buy=0
                maxp=prices[price]
                profit+=maxp-minp
        return profit

        