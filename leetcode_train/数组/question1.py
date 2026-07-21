from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for val , data in enumerate(nums):
            temp = target - data
            if temp in hash_map:
                return [hash_map[temp],val]
            hash_map[data] = val
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)  # 输出: [0, 1]