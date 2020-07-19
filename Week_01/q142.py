# 第一遍自己的代码，使用集合
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        p = head
        while p:
            if p in visited:
                return p
            visited.add(p)
            p = p.next

        return None

# 使用快慢指针
# 这个方法不会啊，还要找入口点，感觉是神仙想出来的
