class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 1. 处理符号
        if numerator == 0:
            return "0"

        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        # 2. 全部转为正数处理，防止取模时出现负数索引问题
        # 注意：Python 的取模结果符号与除数一致，转为 abs 更安全
        num = abs(numerator)
        den = abs(denominator)

        # 3. 计算整数部分
        integer_part = num // den
        res.append(str(integer_part))

        remainder = num % den

        # 如果没有余数，直接返回整数结果
        if remainder == 0:
            return "".join(res)

        # 加上小数点
        res.append(".")

        # 4. 哈希表记录余数出现的位置，用于检测循环
        # key: 余数, value: 当前结果字符串的长度（即小数点的位置）
        seen = {}


        # 5. 模拟长除法，计算小数部分
        # 题目隐含限制：如果长度超过 10^4，则停止
        max_len = 10 ** 4

        while remainder != 0 :
            # 如果长度超过 10^4，按题目要求截断
            if len(res) >= 10 ** 4:
                break

            # 如果当前余数已经出现过，说明找到循环节了
            if remainder in seen:
                # 在记录的位置插入左括号
                res.insert(seen[remainder], "(")
                res.append(")")
                break

            # 【关键】记录位置时，必须包含小数点！
            # 例如 1/6 = 0.1(6)，余数 4 是在小数点后出现的，索引应该是 2
            seen[remainder] = len(res)

            # 下一位计算
            remainder *= 10
            digit = remainder // den
            res.append(str(digit))
            remainder %= den

        return "".join(res)




if __name__ == '__main__':
    s = Solution()
    numerator = 2147483647
    denominator = 37
    print(s.fractionToDecimal(numerator, denominator))