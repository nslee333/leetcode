class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        
        
        
        
        # Brute force algorithm, o(N^2) time complexity
        # ! this solution is too slow.
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         current = prices[j] - prices[i]
        #         max_profit = max(max_profit, current)
        # return max_profit