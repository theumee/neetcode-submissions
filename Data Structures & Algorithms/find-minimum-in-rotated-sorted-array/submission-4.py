class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 999999999

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r-l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
            res = min(nums[m], res)
        return res
