class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        for day in range(len(prices)):
            if prices[day] < prices[buy]:
                buy = day
            else:
                sell = day
                profit = max(profit, prices[sell] - prices[buy])
        
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        
        return profit