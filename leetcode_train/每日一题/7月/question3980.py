from typing import List


class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        # 边界条件检查
        if len(s1) != len(s2):
            return -1
        if s1 == '1' and s2 == '0':
            return -1

        # 将字符串转为列表以便修改
        s1_list = list(s1)
        n = len(s1_list)
        opers = 0

        for i in range(n):
            if s1_list[i] == s2[i]:
                continue

            if s1_list[i] == '0' and s2[i] == '1':
                # 情况1：0→1，直接翻转当前位
                s1_list[i] = '1'
                opers += 1
            else:  # s1_list[i] == '1' and s2[i] == '0'
                # 情况2：1→0
                if i + 1 < n and s1_list[i + 1] == '1':
                    # 如果下一位是1，翻转当前位和下一位（一次操作将两个1变0）
                    s1_list[i] = '0'
                    s1_list[i + 1] = '0'
                    opers += 1
                else:
                    # 否则只能翻转当前位（1变0）
                    s1_list[i] = '0'
                    opers += 1

        return opers
if __name__ == '__main__':
    s = Solution()
    s1 = "11"
    s2 = "00"
    print(s.minOperations(s1, s2))  # 输出: 1