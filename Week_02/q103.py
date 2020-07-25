# 第一遍
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        level = 0
        queue = collections.deque()
        if root: queue.append(root)

        while queue:
            level += 1
            n = len(queue)
            cur_level = []
            for _ in range(n):
                cur_level.append(queue[0].val)
                if queue[0].left: queue.append(queue[0].left)
                if queue[0].right: queue.append(queue[0].right)
                queue.popleft()
            # 通过奇偶判断正序or倒序
            ret.append(cur_level if level % 2 else cur_level[-1::-1])
        
        return ret
