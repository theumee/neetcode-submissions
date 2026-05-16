class MinStack:

    def __init__(self):
        self.stk = []
        self.minStk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.minStk) == 0 or val <= self.minStk[-1]:
            self.minStk.append(val)

    def pop(self) -> None:
        if self.stk:
            val = self.stk.pop()
            if self.minStk and val == self.minStk[-1]:
                self.minStk.pop()
        

    def top(self) -> int:
        return self.stk[len(self.stk) - 1]
        

    def getMin(self) -> int:
        return self.minStk[len(self.minStk) - 1]