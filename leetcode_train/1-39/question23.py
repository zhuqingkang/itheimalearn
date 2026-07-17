from typing import List,Optional
from itheimalearn.leetcode_train.data_structure.ListNode_defined import ListNode

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # 分治合并
        interval = 1
        n = len(lists)

        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]

    def mergeTwoLists(self, param :Optional[ListNode], param1:Optional[ListNode]):
        if not param : return param1
        if not param1 : return param
        if param.val <= param1.val:
            param.next = self.mergeTwoLists(param.next, param1)
            return param
        else:
            param1.next = self.mergeTwoLists(param, param1.next)
            return param1
