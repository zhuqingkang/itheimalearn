class Solution:
    # ---- 基础版：双指针，O(|t|) 时间，O(1) 空间 ----
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


class SolutionAdvanced:
    """
    进阶版：处理 k >= 10 亿次查询。
    思路：预处理 t，构建「下一个字符位置」跳表 dp，
          使得每次查询只需 O(|s|) 时间。
    """

    def __init__(self, t: str):
        self.t = t
        self.n = len(t)
        # dp[i][c] = 从 t 中下标 i 开始，字符 c 首次出现的位置；不存在则为 -1
        # dp 大小为 (n+1) × 26，dp[n] 全 -1 表示末尾之后不存在任何字符
        self.dp = [[-1] * 26 for _ in range(self.n + 1)]

        # 从右向左填充 dp
        for i in range(self.n - 1, -1, -1):
            for c in range(26):
                self.dp[i][c] = self.dp[i + 1][c]
            char_idx = ord(self.t[i]) - ord('a')
            self.dp[i][char_idx] = i

    def check(self, s: str) -> bool:
        """O(|s|) 查询 s 是否为 t 的子序列"""
        pos = 0  # 当前在 t 中的搜索起点
        for ch in s:
            c = ord(ch) - ord('a')
            nxt = self.dp[pos][c]
            if nxt == -1:
                return False
            pos = nxt + 1  # 下次从匹配位置之后开始搜
        return True


# ---------- 测试 ----------
if __name__ == "__main__":
    # 基础版测试
    sol = Solution()
    print(sol.isSubsequence("abc", "ahbgdc"))   # True
    print(sol.isSubsequence("axc", "ahbgdc"))   # False

    # 进阶版测试
    t = "ahbgdc"
    adv = SolutionAdvanced(t)
    queries = ["abc", "axc", "bg", "aa", "", "dc", "ahbgdc"]
    for s in queries:
        print(f"isSubsequence('{s}', '{t}') = {adv.check(s)}")
