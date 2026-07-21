class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        result = n
        count = 0
        while result >= 5:
            result = result // 5
            count += result
        return count

if __name__ == '__main__':
    s = Solution()
    num = 10000
    print(s.trailingZeroes(num))
