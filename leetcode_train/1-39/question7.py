class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        int_max = 2147483647
        int_min = -2147483648

        result = 0
        sign = 1 if x>0 else -1
        x = abs(x)
        while x:
            digit = x % 10  # 求取个位数字
            x //= 10        # 去除各位数字
            result = result * 10 + digit   # 将之前的结果进一位加上本次循环的个位数

        result *= sign
        if result > int_max:
            return 0
        elif result < int_min:
            return 0
        else:
            return result

        # INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        #
        # result = 0
        # sign = -1 if x < 0 else 1
        # x = abs(x)
        #
        # while x != 0:
        #     digit = x % 10
        #     x //= 10
        #
        #     # 溢出检测（关键）
        #     if result > (INT_MAX - digit) // 10:
        #         return 0
        #
        #     result = result * 10 + digit
        #
        # return sign * result