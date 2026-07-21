class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        i = 1  # 初始处理个位（10^0）
        while i <= n:
            divider = i * 10  # 计算高位分割点（如i=1时，divider=10）
            high = n // divider  # 高位部分
            digit = (n // i) % 10  # 当前位的数字
            low = n % i  # 低位部分

            if digit < 1:
                count += high * i
            elif digit == 1:
                count += high * i + low + 1
            else:
                count += (high + 1) * i

            i *= 10  # 处理下一位（十位、百位等）
        return count

