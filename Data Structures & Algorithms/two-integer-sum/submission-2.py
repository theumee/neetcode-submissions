class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if count.get(diff) != None:
                return [count[diff],i]
            count[nums[i]] = i
        return None
