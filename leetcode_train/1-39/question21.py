from typing import List,Optional
from itheimalearn.leetcode_train.data_structure.ListNode_defined import ListNode

# 递归

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2  # 终止条件，直到两个链表都空
        if not list2: return list1
        if list1.val <= list2.val:  # 递归调用
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2