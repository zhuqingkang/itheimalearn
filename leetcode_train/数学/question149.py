from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:


        # 正常推导
        if len(points) < 3: return len(points)

        max_num = 0
        for i in range(len(points)):
            same = 1
            for j in range(i + 1, len(points)):
                count = 0
                if(points[i][0]==points[j][0] and points[i][1]==points[j][1]):
                    same+=1
                else:
                    count += 1
                    x_diff = points[i][0] - points[j][0]
                    y_diff = points[i][1] - points[j][1]

                    for k in range(j + 1, len(points)):
                        if (x_diff * (points[i][1] - points[k][1])) == (y_diff * (points[i][0] - points[k][0])) :
                            count += 1
                max_num = max(max_num, same+count)

            if (max_num > len(points) / 2): return max_num

        return max_num

        # 反证法先假设
        ans = 0
        for i, (x, y) in enumerate(points):  # 假设直线一定经过 points[i]
            cnt = defaultdict(int)  # 先使用内置函数创建一个字典
            
            for x2, y2 in points[i + 1:]:
                dx, dy = x2 - x, y2 - y
                k = dy / dx if dx else inf
                cnt[k] += 1
                ans = max(ans, cnt[k])  # 这里没有算上 (x,y) 这个点，最后再加一
        return ans + 1