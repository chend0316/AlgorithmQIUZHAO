#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#
# https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/description/
#
# algorithms
# Medium (34.40%)
# Likes:    56
# Dislikes: 0
# Total Accepted:    10.4K
# Total Submissions: 30.1K
# Testcase Example:  '[[0,1],[1,0]]'
#
# 在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。
# 
# 一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：
# 
# 
# 相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角）
# C_1 位于 (0, 0)（即，值为 grid[0][0]）
# C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]）
# 如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0）
# 
# 
# 返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 输入：[[0,1],[1,0]]
# 
# 输出：2
# 
# 
# 
# 示例 2：
# 
# 输入：[[0,0,0],[1,1,0],[1,1,0]]
# 
# 输出：4
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length == grid[0].length <= 100
# grid[i][j] 为 0 或 1
# 
# 
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

# @lc code=end

# 启发式搜索，出队列visited，答案正确
from heapq import heappush, heappop
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        h = lambda i, j: max(N - 1 - i, M - 1 - j)
        queue = []
        if grid[0][0] == 0:
            heappush(queue, (h(0, 0) + 1, 1, (0, 0)))
            visited = set()
        while queue:
            _, depth, cur = heappop(queue)
            if cur in visited: continue  #
            visited.add(cur)  # 出队列visited，答案正确
            curx, cury = cur
            if curx == N - 1 and cury == M - 1: return depth 
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                nextx, nexty = curx + dx, cury + dy
                nex = nextx, nexty
                if 0 <= nextx < N and 0 <= nexty < M and grid[nextx][nexty] == 0:
                    heappush(queue, (h(nex[0], nex[1]) + depth + 1, depth + 1, nex))
        return -1

# 启发式搜索，入队列visited，答案错误 
# [[0,0,0,0,1,1,1,1,0],[0,1,1,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,0],[1,1,0,0,1,0,0,1,1],[0,0,1,1,1,0,1,0,1],[0,1,0,1,0,0,0,0,0],[0,0,0,1,0,1,0,0,0],[0,1,0,1,1,0,0,0,0],[0,0,0,0,0,1,0,1,0]]
# 期望的是11，但输出的是12
from heapq import heappush, heappop
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        h = lambda i, j: max(N - 1 - i, M - 1 - j)
        queue = []
        if grid[0][0] == 0:
            heappush(queue, (h(0, 0) + 1, 1, (0, 0)))
            visited = {(0, 0)}
        while queue:
            _, depth, cur = heappop(queue)
            curx, cury = cur
            if curx == N - 1 and cury == M - 1: return depth 
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                nextx, nexty = curx + dx, cury + dy
                nex = nextx, nexty
                if 0 <= nextx < N and 0 <= nexty < M and nex not in visited and grid[nextx][nexty] == 0:  #
                    heappush(queue, (h(nex[0], nex[1]) + depth + 1, depth + 1, nex))
                    visited.add(nex)  # 入队列visited，答案错误
        return -1

# 非启发式搜索
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        queue = []
        if grid[0][0] == 0:
            queue.append((0, 0))
            visited = {(0, 0)}
            res = 0
        while queue:
            tmp = []
            res += 1
            for curx, cury in queue:
                if curx == N - 1 and cury == M - 1: return res
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    nextx, nexty = curx + dx, cury + dy
                    if 0 <= nextx < N and 0 <= nexty < M and (nextx, nexty) not in visited and grid[nextx][nexty] == 0:
                        tmp.append((nextx, nexty))
                        visited.add((nextx, nexty))
            queue = tmp
        return -1