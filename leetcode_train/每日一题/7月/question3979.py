from typing import List

class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_num = 0

        for i in range(n-1):
            left = i
            right = n-1
            while left < right and right - left >= k:
                new_num = nums[left] + nums[right]
                max_num = max(max_num, new_num)

                right -= 1

        return max_num

if __name__ == '__main__':
    nums = [1, 3, 5, 2, 8]
    k = 2
    s = Solution()
    print(s.maxValidPairSum(nums, k))