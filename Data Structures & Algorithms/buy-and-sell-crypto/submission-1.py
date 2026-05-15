class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for each in prices:
            profit = each - buy
            buy = min(buy, each)
            max_profit = max(max_profit, profit)
        return max_profit
            
        