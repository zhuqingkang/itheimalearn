from itheimalearn.leetcode_train.data_structure.ListNode_defined import ListNode
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(-1)   # 不管怎么删除就算删除的是头节点也会指向新的头节点
        dummy_node.next = head

        ### 先走n步，然后双指针走到末尾，删除下一个
        p1 = dummy_node     # 当前选中的是头节点前面的空值
        for _ in range(n + 1):  # 要删除倒数第n个节点所以p1节点先向后位 n+1 个位置 因为后面判定的时候需要
            p1 = p1.next

        p2 = dummy_node
        while p1:  # 当 p1 选中的值是 none 也就是  最后一个节点后面的 时候退出
            p1 = p1.next
            p2 = p2.next

        # 删除要删除的值
        p2.next = p2.next.next

        return dummy_node.next


"""
[] -> [] -> [] -> .... -> []

假如这是一个链表
可以把dummy这类指针看成一个抽象的那个数值属性
首先
[dummy] -> [] -> [] -> [] -> .... -> []
然后创建p1
[dummy,p1] -> [] -> [] -> [] -> .... -> []
因为要删除倒数第n个节点
所以p1先往后位移 n+1 个值，这样只有在到位置的时候p1刚好是空值
这里距离就是n = 2
执行完就是
[dummy] -> [] -> [] -> [p1] -> .... -> []
后面创建p2
[dummy,p2] -> [] -> [] -> [p1] -> .... -> []
然后他们同时移动
[dummy] -> [] -> [] -> [] -> .... -> [p2] -> [-2] -> [-1] ->None(p1)
当p1是空值的时候跳出循环
这时候我们要删除的数值就是我们的
p2.next 
然后我们将指针指向后一个位置
p2.next = p2.next.next
[dummy] -> [] -> [] -> [] -> .... -> [p2]  -> [-1] ->None(p1)
就是指向的下一个指向下一个的下一个。
"""
