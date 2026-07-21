from typing import List

class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid = len(nums) // 2
        count_num = nums.count(nums[mid])
        if count_num == 1:
            return True
        else:
            return False