

from itheimalearn.leetcode_train.data_structure.ListNode_defined import ListNode
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            vall1 = l1.val if l1 is not None else 0
            vall2 = l2.val if l2 is not None else 0

            total = vall1 + vall2+carry

            carry = total // 10

            prev.next = ListNode(total % 10)

            prev = prev.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
'''
我原来的想法是创建一个虚拟头节点 然后遍历各个节点然后对遍历方式不太熟悉发生了错误，且指针当时没有发生改动
这是大模型给出的参考答案 运行效率一般不过逻辑条理清楚比较好理解
'''


