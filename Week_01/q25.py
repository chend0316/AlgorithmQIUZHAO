# 第一遍
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        pre_group = dummy
        cur = head

        while cur:
            # input: pre_group, cur
            i = 0
            pre, cur_group = None, cur
            while cur and i < k:
                cur.next, pre, cur = pre, cur, cur.next
                i += 1
            if i == k:
                pre_group.next = pre
                pre_group = cur_group
            else:
                pre, cur = None, pre
                while cur:
                    cur.next, pre, cur = pre, cur, cur.next
                pre_group.next = pre
                break
        
        return dummy.next

# 最后一组可能不需要翻转
# 思路1：最后一组翻转后再翻转回来
# 思路2：先判断最后一组需不需要翻转

# 这个老哥的代码很短
def reverseKGroup(self, head, k):
    dummy = jump = ListNode(0)
    dummy.next = l = r = head
    
    while True:
        count = 0
        while r and count < k:   # use r to locate the range
            r = r.next
            count += 1
        if count == k:  # if size k satisfied, reverse the inner linked list
            pre, cur = r, l
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur  # standard reversing
            jump.next, jump, l = pre, l, r  # connect two k-groups
        else:
            return dummy.next
