from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = 0
        for i in range(len(digits)):
            digit = digit  + digits[i]*10**(len(digits)-i-1)
        digit += 1
        temp = [*str(digit)]
        for i in range(len(temp)):
            temp[i] =int(temp[i])
        return temp

if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1,2,3,4,5]))