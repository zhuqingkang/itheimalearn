from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        data = {'2':'abc','3':'def','4':'ghi',
                '5':'jkl','6':'mno','7':'pqrs',
                '8':'tuv','9':'wxyz'}
        result = ['']

        for digit in digits:
            for  i in range(len(result)):
                temp = result.pop(0)
                for j in data[digit]:
                    result.append(''.join([temp, j]))

        return result
if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
    print(s.letterCombinations('24'))