from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            add = 1 << i  # 计算当前位的高位值（2^i）
            # 反转当前res，每个元素加add后拼接
            res += [x + add for x in reversed(res)]
        return res