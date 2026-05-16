class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        end = len(matrix[0]) - 1
        for nums in matrix:
            if nums[end] == target:
                return True
            elif nums[end] > target:
                if self.bs(nums,target):
                    return True
        return False
        
    def bs(self,arr,t):
        i, j = 0, len(arr) - 1
        while i <= j:
            m = i+ (j-i)//2
            if arr[m] == t:
                return True
            elif arr[m] > t:
                j = m - 1
            else:
                i = m + 1
        return False
