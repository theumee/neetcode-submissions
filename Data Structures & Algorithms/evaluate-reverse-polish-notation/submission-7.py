class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val = int(tokens[0])
        list = []
        for t in tokens:
            print(list)
            if t not in "+-/*":
                list.append(int(t))
            else:
                b = list.pop()
                a = list.pop()
                if t == "+": val = a+b
                if t == "-": val = a-b
                if t == "*": val = a*b
                if t == "/": val = int(a/b)
                list.append(val)
        return val