class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 : return False
        stk = []
        for c in s:
            if c in ['(', '{', '[']:
                stk.append(c)
            elif stk and (ord(c) - ord(stk[-1])) in [1,2]:
                stk.pop()
            else:
                return False
        return len(stk) == 0;

