class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,n in enumerate(nums):
            diff = target - n
            if map.get(diff) != None:
                return [map.get(diff), i]
            map[n] = i
        return []