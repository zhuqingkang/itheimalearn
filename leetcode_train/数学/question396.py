from typing import List

# class Solution:
#     def maxRotateFunction(self, nums: List[int]) -> int:
#         n = len(nums)
#         res = []

#         for i in range(n):
#           temp = self.fanzhuan(nums,i)
#           for j in range(len(temp)):
#             temp[j] = temp[j] * j
#           res.append(sum(temp))

#         return max(res)
#     @staticmethod
#     def fanzhuan(nums,k):
#         n = len(nums)
#         k = k % n
#         return nums[n - k:] + nums[:n - k]
# 优化后的

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # 计算 F(0)
        total_sum = sum(nums)
        F0 = sum(i * val for i, val in enumerate(nums))

        max_val = F0
        prev_F = F0

        # 递推计算所有 F(k)
        for k in range(1, n):
            # F(k) = F(k-1) + total_sum - n * nums[n-k]
            prev_F = prev_F + total_sum - n * nums[n - k]
            max_val = max(max_val, prev_F)

        return max_val

if __name__ == "__main__":
    nums = [4, 3, 2, 6]
    solution = Solution()
    print(solution.maxRotateFunction(nums))  # 输出: 26