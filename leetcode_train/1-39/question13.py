class Solution:
    def romanToInt(self, s: str) -> int:
        value = {"I" : 1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result = 0
        for i in range(len(s)-1):
            if value[s[i]] < value[s[i+1]]:
                result -= value[s[i]]
            else:
                result += value[s[i]]
        return result+value[s[-1]]

"""
先创建字典
然后进行遍历（没有最后一个的值）看看当前的是否比后一个小，
如果小减去当前数值否则就加上当前数值
最后返回result+=value[s[-1]]
"""