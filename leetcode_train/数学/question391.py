from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        total_area = 0
        corners = set()

        for x1, y1, x2, y2 in rectangles:
            total_area += (x2 - x1) * (y2 - y1)

            # 异或操作：偶数次出现会抵消，奇数次保留
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)

        # 必须恰好剩4个角点
        if len(corners) != 4:
            return False

        # 验证这4个点构成外接矩形
        xs = [x for x, _ in corners]
        ys = [y for _, y in corners]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)

        bounding_area = (max_x - min_x) * (max_y - min_y)
        return total_area == bounding_area

if __name__ == "__main__":
    solution = Solution()
    rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
    print(solution.isRectangleCover(rectangles))  # 输出: True