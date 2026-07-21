class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        def dfs(n):
            if n == 1:
                return True
            elif n<1:
                return False
            n = n / 2
            return dfs(n)
        return dfs(n)

if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(8))