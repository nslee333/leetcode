# ^ Neetcode #1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                current = prices[r] - prices[l]
                max_profit = max(max_profit, current)
            else:
                l = r
            r += 1
        return max_profit

# ^ Neetcode #2 - 100ms faster than 
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
    # res = 0
    #     lowest = prices[0]
    #     for price in prices:
    #         if price < lowest:
    #             lowest = price
    #         res = max(res, price - lowest)
    #     return res
    
#  ^ My brute force idea, o(N^2) time complexity
# ! this idea is too slow, not a solution
# max_profit = 0
# for i in range(len(prices)):
#     for j in range(i + 1, len(prices)):
#         current = prices[j] - prices[i]
#         max_profit = max(max_profit, current)
# return max_profit