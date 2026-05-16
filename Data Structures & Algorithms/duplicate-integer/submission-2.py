class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for i in nums:
            numSet.add(i)
        return len(numSet) != len(nums)