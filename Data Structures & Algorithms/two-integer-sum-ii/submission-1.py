class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            summ = nums[r] + nums[l]
            if summ == t:
                return [l+1,r+1]
            if summ > t:
                r-=1
            if summ < t:
                l+=1
        return []