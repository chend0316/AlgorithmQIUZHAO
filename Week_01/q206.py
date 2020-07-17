# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # if not head: return None
        prev = None
        cur = head

        while cur:
            # 一开始这样写，然后翻车了！
            # cur, cur.next, prev = cur.next, prev, cur

            # 下面3种都正确
            # cur.next, cur, prev = prev, cur.next, cur
            # prev, cur.next, cur = cur, prev, cur.next
            cur.next, prev, cur = prev, cur, cur.next

        return prev
