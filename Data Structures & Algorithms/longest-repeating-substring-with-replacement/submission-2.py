class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l , r , res, maxFreq = 0 , 0 , 0 , 0
        while r < len(s):
            counts[s[r]] = counts.get(s[r],0) + 1
            maxFreq = max(maxFreq, counts[s[r]])
            if (r-l+1) - maxFreq > k:
                counts[s[l]] = counts.get(s[l]) - 1
                l+=1
            res = max(res,r-l+1)
            r+=1
        return res