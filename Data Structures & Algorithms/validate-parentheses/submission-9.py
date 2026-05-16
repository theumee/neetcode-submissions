class Solution:
    def isValid(self, val: str) -> bool:
        if len(val) %2 !=0 : return False
        stk = []
        for s in val:
            if stk and (ord(s) - ord(stk[-1])) in [1,2]:
                stk.pop()
            elif s in "{[(":
                stk.append(s)
            else:
                return False
        return len(stk) == 0
