
# sliding window solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = l + 1
        max_value = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_value = max(max_value, profit)
            else:
                l = r
            r += 1
        return max_value


# neetcode dynamic programming solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_price = 0
        min_price = prices[0]

        for price in prices:
            max_price = max(max_price, price - min_price)
            min_price = min(min_price, price)
        return max_price