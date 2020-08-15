#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode-cn.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (42.15%)
# Likes:    350
# Dislikes: 0
# Total Accepted:    66.9K
# Total Submissions: 158.8K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
# 
# 示例:
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# 运行你的函数后，矩阵变为：
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# 解释:
# 
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]: return
        N, M = len(board), len(board[0])
        if N <= 2 or M <= 2: return
        ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j):
            if 0 <= i < N and 0 <= j < M and board[i][j] == 'O':
                board[i][j] = 'A'
                for dx, dy in ds:
                    dfs(i + dx, j + dy)

        i, j = 0, 0
        for dx, dy in ds:
            while True:
                dfs(i, j)
                if 0 <= i + dx < N and 0 <= j + dy < M:
                    i, j = i + dx, j + dy
                else:
                    break

        for i in range(N):
            for j in range(M):
                if board[i][j] == 'A': board[i][j] = 'O'
                elif board[i][j] == 'O': board[i][j] = 'X'

# @lc code=end

