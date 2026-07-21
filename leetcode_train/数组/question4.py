from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mn = nums1+nums2
        mn.sort()
        n = len(mn)
        if n%2!=0:
            return mn[n//2]
        else:
            return (mn[n//2]+mn[n//2-1])/2

if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2,4]
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 2.0