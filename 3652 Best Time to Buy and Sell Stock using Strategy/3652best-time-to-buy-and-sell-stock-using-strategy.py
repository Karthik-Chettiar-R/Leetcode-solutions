class Solution(object):
    def maxProfit(self, prices, strategy, k):
        n = len(prices)
        
        prefix_prices = [0] * (n + 1)
        prefix_original_profits = [0] * (n + 1)

        for i in range(n):
            prefix_prices[i+1] = prefix_prices[i] + prices[i]
            prefix_original_profits[i+1] = prefix_original_profits[i] + prices[i] * strategy[i]
        
        original_profit = prefix_original_profits[n]
        max_profit = original_profit
        
        for i in range(n - k + 1):
            old_window_profit = prefix_original_profits[i + k] - prefix_original_profits[i]
            
            new_window_profit = prefix_prices[i + k] - prefix_prices[i + k // 2]
            
            current_profit = original_profit - old_window_profit + new_window_profit

            if current_profit > max_profit:
                max_profit = current_profit
                
        return max_profit
