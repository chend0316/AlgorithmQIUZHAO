# 第一遍
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

# 第二遍
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p, pre = head, None
        while p:
            p.next, pre, p = pre, p, p.next
        return pre
