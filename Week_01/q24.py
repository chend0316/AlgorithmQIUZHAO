# 第一遍自己的代码
# 参考国际站发现了一些问题
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        a, b = head, head.next
        res = prev = ListNode()  # 问题：对于“哨兵”变量，变量名可以叫做dummy
        prev.next = head

        while a and b:
            prev.next = b
            prev = a
            a.next, b.next, a = b.next, a, b.next
            b = a.next if a else None
            # 问题：a、b都可以通过prev计算得到，将循环变量改为prev，可以让代码更清晰（循环变量从2个减少为1个）

        return res.next

# 继续改进
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode()
        prev.next = head

        while prev.next and prev.next.next:
            a, b = head, head.next
            a.next, b.next, prev.next = b.next, a, b
            prev = a

        return dummy.next

# 第二遍代码
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            a, b = pre.next, pre.next.next
            a.next, b.next, pre.next = b.next, a, b
            pre = a
        return dummy.next
