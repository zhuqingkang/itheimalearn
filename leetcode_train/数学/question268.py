from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 方法1：异或法
      def method1(nums):
        res = len(nums)
        for i in range(len(nums)):
            res ^= nums[i] ^ i
        return res

      # 方法2：排序+遍历
      def method2(nums):
        n = len(nums)
        nums.sort()
        for i in range(n+1):
            if i not in nums:
              return i

if __name__ == "__main__":
    solution = Solution()
    nums = [3, 0, 1]
    print(solution.missingNumber(nums))  # Output: 2