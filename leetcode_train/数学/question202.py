class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def dfs(n):
            if n == 1:
                return True

            if n in seen:
                return False
            seen.add(n)

            result = 0
            while n:
                digit = n % 10
                result += digit ** 2
                n //= 10

            return dfs(result)

        return  dfs(n)

if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(2))