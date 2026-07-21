class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s1) == 1:
            if s2.find(s1)+1 :
                return True
        try:
            temp = s1[::-1]
            print(temp)
            if s2.index(temp):
                return True
        except ValueError:
            return False

if __name__ == "__main__":
    s1 = "a"
    s2 = "ab"
    solution = Solution()
    result = solution.checkInclusion(s1, s2)
    print(result)  # 输出: True