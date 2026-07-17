class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0 
        min_price = float("inf")
        for i in range (0,n):
            min_price = min(min_price,prices[i])
            max_profit = max(max_profit,prices[i] - min_price)
        return max_profit
        # max_minus = 0

        # for i in range (0,n-1):
        #     minus = 0
        #     for j in range (i+1,n):
        #         minus = prices[j] - prices[i]
        #         if minus>max_minus:
        #             max_minus = minus
        # return max_minus