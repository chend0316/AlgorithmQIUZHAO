# 第一遍
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        p = dummy

        while l1 and l2:
            if l1.val < l2.val:
                p.next, l1 = l1, l1.next
            else:
                p.next, l2 = l2, l2.next
            p = p.next
        while l1:
            p.next, l1 = l1, l1.next
            p = p.next
        while l2:
            p.next, l2 = l2, l2.next
            p = p.next

        return dummy.next