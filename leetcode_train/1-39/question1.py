from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for val,date in enumerate(nums):
            complement = target - date
            if complement in hashmap:
                return [hashmap[complement], val]
            hashmap[date] = val
'''
出现查找缺失值的时候可以考虑用  - > 哈希表
'''