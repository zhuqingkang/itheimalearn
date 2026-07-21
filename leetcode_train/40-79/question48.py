from typing import List
import numpy as np
import pandas as pd


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        df = pd.DataFrame(matrix)
        df_T = df.T  # 转置
        df_rotated = df_T.iloc[:,::-1]   # 进行翻转操作
        print(df_rotated.values.tolist())  # 转回列表格式

        df = pd.DataFrame(matrix)
        # 转置 + 反转列顺序 = 顺时针旋转90度
        result = pd.DataFrame(np.rot90(df.values, k=-1))
        matrix = df_rotated.values.tolist()
        print(matrix)


        n = len(matrix)
        # 转置
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 反转
        for i in range(n):
            matrix[i].reverse()

        print(matrix)


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(matrix)