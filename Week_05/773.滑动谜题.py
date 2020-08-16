#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#
# https://leetcode-cn.com/problems/sliding-puzzle/description/
#
# algorithms
# Hard (60.46%)
# Likes:    83
# Dislikes: 0
# Total Accepted:    3.9K
# Total Submissions: 6.5K
# Testcase Example:  '[[1,2,3],[4,0,5]]'
#
# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
# 
# 一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
# 
# 最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
# 
# 给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
# 
# 示例：
# 
# 
# 输入：board = [[1,2,3],[4,0,5]]
# 输出：1
# 解释：交换 0 和 5 ，1 步完成
# 
# 
# 
# 输入：board = [[1,2,3],[5,4,0]]
# 输出：-1
# 解释：没有办法完成谜板
# 
# 
# 
# 输入：board = [[4,1,2],[5,0,3]]
# 输出：5
# 解释：
# 最少完成谜板的最少移动次数是 5 ，
# 一种移动路径:
# 尚未移动: [[4,1,2],[5,0,3]]
# 移动 1 次: [[4,1,2],[0,5,3]]
# 移动 2 次: [[0,1,2],[4,5,3]]
# 移动 3 次: [[1,0,2],[4,5,3]]
# 移动 4 次: [[1,2,0],[4,5,3]]
# 移动 5 次: [[1,2,3],[4,5,0]]
# 
# 
# 
# 输入：board = [[3,2,4],[1,5,0]]
# 输出：14
# 
# 
# 提示：
# 
# 
# board 是一个如上所述的 2 x 3 的数组.
# board[i][j] 是一个 [0, 1, 2, 3, 4, 5] 的排列.
# 
# 
#

# @lc code=start

# @lc code=end

# A* 搜索
from heapq import heappush, heappop
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        goal_pos = { 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 0: 5 }
        # 估价函数到底怎么选啊，实在搞不懂了
        # h = lambda state: sum([abs(goal_pos[i] - state.index(i)) for i in range(6)])  # 这个不行
        h = lambda state: 5 - state.index(0)

        board = board[0] + board[1]
        moves = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]
        queue, visited = [], set()
        heappush(queue, (0, tuple(board), 0))
        while queue:
            _, cur, cost = heappop(queue)
            visited.add(cur)
            if cur == (1, 2, 3, 4, 5, 0): return cost
            idx1 = cur.index(0)
            for idx2 in moves[idx1]:
                next = list(cur)
                next[idx1], next[idx2] = next[idx2], next[idx1]
                next = tuple(next)
                if next in visited: continue
                heappush(queue, (h(next) + cost + 1, next, cost + 1))
        return -1
