class Solution:
    def addDigits(self, num: int) -> int:

        def dfs(num):
          if num < 10:
              return num
          result = 0
          while num :
              temp = num % 10  # 求个位数

              num = num // 10  # 删除个位数

              result += temp  # 个位数相加

          return dfs(result)

        return dfs(num)

if __name__ == "__main__":
    s = Solution()
    print(s.addDigits(2))
    print(s.addDigits(38))  # Output: 2
    print(s.addDigits(0))   # Output: 0
    print(s.addDigits(12345))  # Output: 6