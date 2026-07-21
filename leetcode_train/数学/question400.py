class Solution:
    def findNthDigit(self, n: int) -> int:
        temp = ""
        if n < 10:
            return n
        for i in range(1, n + 1):
            temp += str(i)
        List_temp = list(temp)
        return int(List_temp[n - 1])
class Solution:
    def findNthDigit(self, n: int) -> int:
        # 确定位数
        digit = 1
        count = 9  # 当前位数的数字个数
        start = 1  # 当前位数的起始数字

        # 找到n所在的位数区间
        while n > digit * count:
            n -= digit * count
            digit += 1
            count *= 10
            start *= 10

        # 现在n表示从start开始的第n位（1-based）
        # 计算是哪个数字
        number = start + (n - 1) // digit

        # 计算是该数字的第几位（从高位到低位，0-based）
        index = (n - 1) % digit

        # 返回对应数字
        return int(str(number)[index])
    
if __name__ == "__main__":
    solution = Solution()
    n = 60
    result = solution.findNthDigit(n)
    print(result)  # Output: 0