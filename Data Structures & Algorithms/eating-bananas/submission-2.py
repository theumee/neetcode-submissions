class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        l = -(-total//h)
        r = max(piles)
        res = r
        while l<=r:
            m = l +(r-l)//2
            hrs = 0
            for pile in piles:
                hrs += (pile + m - 1) // m
            if hrs <= h:
                r = m - 1
                res = m
            else:
                l = m+1

        return res



