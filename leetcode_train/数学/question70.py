class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
            # 初始化前两个状态：a对应f(n-2)，b对应f(n-1)
        a, b = 1, 2
        # 从第3阶迭代到第n阶，共执行 n-2 次
        for _ in range(3, n + 1):
            a, b = b, a + b  # 每次更新：a变为原b，b变为原a+b
        return b