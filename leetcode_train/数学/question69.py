import math


class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0: return 0

        ans = int(math.exp(0.5 * math.log(x)))

        return ans+1 if (ans+1)*(ans+1 )<= x else ans

"""
袖珍计算器 sqrt（x） = math.exp(0.5 * math.log(x))
"""

def mySqrt_double( x: int) -> int:
    l,r,ans = 0,x,-1

    while l<=r:
        mid = (l+r)//2
        if mid**2<=x:
            ans = mid
            l = mid+1
        else:
            r = mid-1
    return ans
"""
二分查找法
"""