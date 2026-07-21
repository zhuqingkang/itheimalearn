class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        data = dict(zip( "ABCDEFGHIJKLMNOPQRSTUVWXYZ" , range(1,27)))
        length = len(columnTitle)
        res = 0
        if length == 1:
            return data.get(columnTitle)
        for i in range(length):
            res +=  data[columnTitle[i]] * 26 ** (length-i-1)

        return res

if __name__ == '__main__':
    s = Solution()
    num = "ZY"
    print(s.titleToNumber(num))