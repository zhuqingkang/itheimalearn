class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        data = {'(':')','[':']','{':'}'}

        for char in s:
            if char in data:
                temp.append(char)
            elif not(temp and data[temp.pop()] == char):
                return False

        return not temp

"""
初始化一个堆 temp
将要用到的数据写到data里

遍历输入的字符串s
如果在data里面看到了就 压入堆 中

否责 就将之前已经压入堆的弹出最顶上的那个
然后在data找到它对应的值 和当前的字符做对比 看看是否匹配 ，
不匹配就返回 false  , 
其中not (temp and .....) 这部分代码是为了提高代码健壮性不让它报错，
因为当temp是空的时候直接就是not(false and ..)也就是True了 
如果最后如果都匹配上了，这时候堆里面的数据都pop()出来完了
这时候temp是False ， not temp 就是 True
"""