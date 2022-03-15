class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for day, _ in enumerate(prices[:-1]):
            if prices[day] < prices[day + 1]:
                profit += prices[day + 1] - prices[day]

        return profit
    
    def maxProfit(self, prices: List[int]) -> int:
        return sum([prices[day + 1] - prices[day] for day in range(len(prices) - 1) if prices[day + 1] - prices[day] > 0])

    def maxProfit(self, prices: List[int]) -> int:
        return sum([max(0, prices[day + 1] - prices[day]) for day in range(len(prices) - 1)])