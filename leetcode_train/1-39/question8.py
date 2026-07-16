import re

class Solution:
    def myAtoi(self, s: str) -> int:
        m = re.match(r'^\s*([+-]?\d+)', s)

        if not m:
            return 0

        num = int(m.group(1))
        return max(min(num, 2 ** 31 - 1), -2 ** 31)