class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxMoney=0
        for i in range(len(accounts)):
            maxMoney=max(maxMoney,sum(accounts[i]))
        return maxMoney
        