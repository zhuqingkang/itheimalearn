class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        temp = float(numerator) / float(denominator)
        return str(temp)
if __name__ == '__main__':
    s = Solution()
    numerator = 1
    denominator = 2
    print(s.fractionToDecimal(numerator, denominator))