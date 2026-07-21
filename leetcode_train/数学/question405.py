class Solution:
    def toHex(self, num: int) -> str:
        temp = hex(num)

        temp2 = format(temp, 'x')
        return str(temp)

if __name__ == "__main__":
    num = 16
    solution = Solution()
    result = solution.toHex(num)
    print(result)  # Output: 26