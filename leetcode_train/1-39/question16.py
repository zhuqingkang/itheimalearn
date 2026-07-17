from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = nums[0]+nums[1]+nums[2]
        min_distance = abs(closest-target)

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                distance = abs(s - target)

                if distance < min_distance:
                    min_distance = distance
                    closest = s

                if s == target:
                    return target
                elif s < target:
                    l = l + 1
                else:
                    r = r - 1
        return closest