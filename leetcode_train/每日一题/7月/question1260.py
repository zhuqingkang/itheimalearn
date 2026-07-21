from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        for _ in range(k):
            last = grid[-1][-1]
            for i in range(m):
                for j in range(n):
                    grid[i][j], last = last, grid[i][j]

        return grid

if __name__ == "__main__":
    solution = Solution()
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 1
    print(solution.shiftGrid(grid, k))  # Output: [[9,1,2],[3,4,5],[6,7,8]]