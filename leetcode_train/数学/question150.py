from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        依据题目很容易想到使用对来解决问题
        """
        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        stack = []
        for s in tokens:
            if s in operators:
                right, left = stack.pop(), stack.pop()
                stack.append(operators[s](left, right))
            else:
                stack.append(int(s))
        return stack.pop()

if __name__ == '__main__':
    sol = Solution()
    tokens = ["1","2","+","3","*","4","-"]
    print(sol.evalRPN(tokens))

