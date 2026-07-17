from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 邪修方法
        # total =[]
        # if not strs:
        #     return ""
        # temp = zip(*strs)
        # for x in temp:
        #     if set(x) != 1:
        #         break
        #     total.append(x[0])
        # return ''.join(total)

        if not strs:
            return ""
        length_same = strs[0]
        count = len(strs)
        for i in range(count):
            length_same = self.lcp(length_same, strs[i])
            if not length_same:
                break

        return length_same

    def lcp(self, a, b):
        length = min(len(a), len(b))
        index = 0
        while index < length and a[index] == b[index]:
            index += 1
        return a[:index]