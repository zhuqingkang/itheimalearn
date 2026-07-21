class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # from math import comb
        # # 总共需要走 (m-1) 步向下 + (n-1) 步向右
        # # 相当于从 (m+n-2) 步中选择 (m-1) 步向下
        # return comb(m + n - 2, m - 1)
        
        data = [[0] *n for _ in range(m)] # 创建一个 m*n 的表

        # 初始化行列数值
        for i in range(m):
            data[i][0] = 1
        for j in range(n):
            data[0][j] = 1

        # 进行相加填充表格
        for i in range(1, m):
            for j in range(1, n):
                data[i][j] = data[i-1][j] + data[i][j-1]
        return data[-1][-1]

        # 压缩到一维数组可以减少空间复杂度
        # date=[1]*n
        # for i in range(1,m):
        #     for j in range(1,n):
        #         date[i] += date[i-1]
        # return date[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 3))