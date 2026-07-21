from typing import List
import random

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0  # 记录遇到target的次数
        result = -1  # 当前选中的索引

        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                # 以 1/count 的概率选择当前索引
                if random.randint(1, count) == 1:
                    result = i

        return result
if __name__ == "__main__":
    nums = [1, 2, 3, 3, 3]
    solution = Solution(nums)
    target = 3
    print(solution.pick(target))  # 输出: 2、3 或 4，概率相等