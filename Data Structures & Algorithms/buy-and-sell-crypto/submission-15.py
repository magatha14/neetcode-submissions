class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        profit = sell-buy
        for p in prices:
            if p > sell and p-buy > profit:
                sell = p
                profit = sell-buy
            elif p < buy:
                buy = p
                sell = p
        return profit
