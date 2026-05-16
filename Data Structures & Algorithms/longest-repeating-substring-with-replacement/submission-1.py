class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l,r,max_freq,res = 0,0,0,0
        while r < len(s):
            counts[s[r]] = 1 + counts.get(s[r],0)
            max_freq = max(max_freq,counts[s[r]])
            if (r-l+1) - max_freq > k:
                counts[s[l]] = counts.get(s[l],0) - 1
                l+=1
            res = max(res,r-l+1)
            r+=1
        return res