from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1

        last  = nums[target:]
        head = nums[:target]
        temp = last + head
        
        return temp.index(target)

if __name__ == "__main__":
    solution = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(solution.search(nums, target))  # Output: 4