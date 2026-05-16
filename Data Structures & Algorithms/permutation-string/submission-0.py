class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        while r <= len(s2):
            if self.isAnagram(s1,s2[l:r]):
                return True
            l+=1
            r+=1
        return False
            
    def isAnagram(self,s,t):
        count = [0] * 26
        for i in range(len(s)):
            count[ord(t[i]) - ord('a')] +=1
            count[ord(s[i]) - ord('a')] -=1
        for n in count:
            if n != 0:
                return False 
        return True
