from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        while k >= length:
            k %= length
        new_nums = [0] *length

        for i in range(length):
            new_index = (i + k) % length
            new_nums[new_index] = nums[i]

        nums[:] = new_nums
        # 第二种方法
        k %= len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]



