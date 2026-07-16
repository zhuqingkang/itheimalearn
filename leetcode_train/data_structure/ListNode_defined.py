class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def list_to_linkedlist(arr):
        dummy = ListNode(0)
        current = dummy
        for val in arr:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    @staticmethod
    def linkedlist_to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result