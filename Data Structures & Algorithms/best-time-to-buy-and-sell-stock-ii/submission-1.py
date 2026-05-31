class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_window = 0

        l = 0

        for r in range(len(prices)):
            curr_profit = prices[r] - prices[l]

            if r > 0 and prices[r] < prices[r - 1]:
                l = r
                max_profit += curr_window
                curr_window = 0
            else:
                curr_window = max(curr_window, curr_profit)

        max_profit += curr_window

        
        return max_profit