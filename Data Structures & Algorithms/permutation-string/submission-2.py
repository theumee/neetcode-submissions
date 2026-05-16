class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        a = "".join(sorted(s1))
        while r <= len(s2):
            
            b = "".join(sorted(s2[l:r]))
            print(a,b,s2[l:r], l ,r)
            if a == b:
                return True
            l+=1
            r+=1
        return False
