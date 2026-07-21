from typing import Optional
from itheimalearn.leetcode_train.data_structure.ListNode_defined import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummp = ListNode()
        dummp.next = head
        prev = dummp

        while prev.next and prev.next.next:

            first = prev.next
            second = first.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first

        return dummp.next
