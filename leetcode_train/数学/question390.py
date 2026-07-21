class Solution:
    def lastRemaining(self, n: int) -> int:
        """
        数学法：跟踪头部元素 head 和步长 step。
        - 从左到右：头部一定被删，head += step
        - 从右到左：只有剩余奇数个时头部才被删，否则头部不动
        """
        head = 1
        step = 1
        left_to_right = True
        remaining = n

        while remaining > 1:
            if left_to_right or remaining % 2 == 1:
                head += step
            step *= 2
            remaining //= 2
            left_to_right = not left_to_right

        return head
