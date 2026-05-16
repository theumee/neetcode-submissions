class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        l,r,max_freq,res = 0,0,0,0
        while r < len(s):
            index = ord(s[r]) - ord('A')
            counts[index] +=1
            max_freq = max(max_freq,counts[index])
            if (r-l+1) - max_freq > k:
                counts[ord(s[l]) - ord('A')] -=1
                l+=1
            res = max(res,r-l+1)
            r+=1
        return res

        

