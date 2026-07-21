class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        data  = dict(zip(range(1,27),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        if columnNumber <= 26:
            return data.get(columnNumber)
        while columnNumber:
            yushu = columnNumber % 26
            if yushu == 0:   # 考虑到 余数是0或者是26的情况
                yushu = 26
                columnNumber -= 1
            columnNumber = columnNumber // 26
            res.append(data[yushu])
        return "".join(reversed(res))  # 因为是先算个位依次算的 所以需要倒着输出


if __name__ == '__main__':
    s = Solution()
    num1 = 23
    num2 = 701
    # print(s.convertToTitle(num1))
    print(s.convertToTitle(num2))