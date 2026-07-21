from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # m = len(matrix)
        # n = len(matrix[0])
        # hash_map = {}
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] ==0:
        #             hash_map[str(i) + str(j)] =[i,j]
        # for i in hash_map.values():
        #     for j in range(n):
        #         matrix[i[0]][j] = 0
        #     for j in range(m):
        #         matrix[j][i[1]] = 0

        # print(matrix)

        row = [0 in r for r in matrix]
        col = [0 in c for c in zip(*matrix)]

        for i, ro in enumerate(row):
            for j, co in enumerate(col):
                if ro or co:
                    matrix[i][j] = 0

        print(matrix)

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    solution.setZeroes(matrix)