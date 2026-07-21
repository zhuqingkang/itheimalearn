class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 给你两个整数 a 和 b ，不使用 运算符 + 和 - ​​​​​​​，计算并返回两整数之和。
        # 迭代法
        MASK = 0xFFFFFFFF
        a = a & MASK
        b = b & MASK

        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK

        # 若最高位为 1，说明是负数（补码）
        if a & 0x80000000:
            # 转换为 Python 的真负数：~(a ^ MASK)
            return ~(a ^ MASK)
        else:
            return a

