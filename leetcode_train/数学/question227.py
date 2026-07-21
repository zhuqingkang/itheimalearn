class Solution:
    def calculate(self, s: str) -> int:
        a = []
        opmp = {
            "+": lambda e: a.append(e),
            "-": lambda e: a.append(-e),
            "*": lambda e: a.append(e * a.pop()),
            "/": lambda e: a.append(int(operator.truediv(a.pop(), e)))
        }
        op = "+"
        num = 0
        for c in s + "+":
            if c.isdigit():
                num = num * 10 + int(c)
            elif c != " ":
                opmp[op](num)
                op = c
                num = 0
        return sum(a)
