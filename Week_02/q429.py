# 第一遍
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ret = []
        queue = collections.deque()
        if root: queue.append(root)
        while queue:
            ret.append([])
            n = len(queue)
            for _ in range(n):
                ret[-1].append(queue[0].val)
                for child in queue[0].children:
                    queue.append(child)
                queue.popleft()
        return ret