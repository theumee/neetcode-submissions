class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            short = heights[l]
            diff = r-l
            if heights[l] > heights[r]:
                short = heights[r]
                r-=1
            else:
                l+=1
            pr = short * diff
            res = max(pr,res)
        return res