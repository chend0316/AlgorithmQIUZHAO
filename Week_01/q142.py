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
# 要找入口点，需要一些灵感
# 灵感如下：
# 如果一直跑下去，快慢指针会相遇无数次，但每次的相遇点都是同一个。
# 我们让快指针跑两轮直线，慢指针只跑一轮直线，就能确保相遇点正好是入口点。
'''
       入口点
          |
          v
o -- o -- o -- o -- o
          |         |
          o -- o -- o

【延长直线跑道，但我们并不知道该延长几个元素，所以不可行】
      慢指针起跑点
          |     入口点/相遇点
          |         |
          v         v
x -- x -- o -- o -- o -- o -- o
^                   |         |
|                   o -- o -- o
将快指针起跑点延长，使得快指针的直线是慢指针的2倍

【】
'''
