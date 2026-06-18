class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        min_p = 101
        for i in range(1, len(prices)):
            if min_p > prices[i-1]:
                min_p = prices[i-1]
            if best < prices[i] - min_p:
                best = prices[i] - min_p
        return best