class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        nums = [0] * 25
        for i in range(len(s)):
            nums[ord('a') - ord(s[i])]+=1
            nums[ord('a') - ord(t[i])]-=1
        
        for n in nums:
            if n != 0:
                return False
        return True