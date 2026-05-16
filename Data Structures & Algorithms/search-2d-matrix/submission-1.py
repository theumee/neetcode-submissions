class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        end = len(matrix[0]) - 1
        for nums in matrix:
            if nums[end] == target:
                return True
            if nums[end] > target:
                return self.search(nums,target)
            
        return False


    def search(self, nums: List[int], target: int) -> int:
        l,r =0,len(nums) - 1

        while l <= r:
            m = l+(r-l)//2
            if nums[m] == target:
                return True
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False