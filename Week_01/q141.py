# 第一遍自己的代码，集合
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        p = head
        while p:
            if p in visited: return True
            visited.add(p)
            p = p.next
        return False

# 第一遍自己的代码，快慢指针
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# 参考国际站，代码简洁度差不多，不需要改进
