class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 使用列表的内置函数进行排序
        # 然后先判断长度是否一样不一样就直接返回Flase
        l1 = list(s)
        l2 = list(t)
        l1.sort()
        l2.sort()
        if len(l1) != len(l2):
            return False

        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
        return True
        """
        使用词典中的get用法
        """
        dict1 = {}
        dict2 = {}
        for c in s:
            dict1[c] = dict1.get(c, 0) + 1
        for c in t:
            dict2[c] = dict2.get(c, 0) + 1
        return dict1 == dict2

if __name__ == '__main__':
    s = Solution()
    A = "abcdefg"
    B = "abefgcd"
    print(s.isAnagram(A, B))

