class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        return str(x) == str(x)[::-1]

"""
首先 先判断是不是等于零如果等于0 就返回 True
接下来就判断是否小于0或者是对10求余是不是0
两个满足一个就返回Fales
最后将x转化为字符串 先正向取值 ，然后再进行反向取值判断是否相等

"""