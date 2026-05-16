class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i = 0
        j = 1
        while j in range(len(prices)):
            diff = prices[j] - prices[i]
            if diff >= 1:
                j+=1
                res = max(diff, res)
            else:
                i = j
                j = i + 1
        return res

                