#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (49.74%)
# Likes:    681
# Dislikes: 0
# Total Accepted:    135.1K
# Total Submissions: 270.9K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
# 
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 
# 
# 示例 1:
# 
# 输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def initUF(self, n):
        self.uf = [i for i in range(n)]

    def union(self, i, j):
        self.uf[self.find(i)] = self.uf[self.find(j)]
    
    def find(self, i):
        root = i
        while self.uf[root] != root: root = self.uf[root]
        while self.uf[i] != root: self.uf[i], i = root, self.uf[i]
        return root

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        N, M = len(grid), len(grid[0])
        self.initUF(N * M)
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '0': continue
                for dx, dy in self.dxdy:
                    if 0 <= i + dx < N and 0 <= j + dy < M and grid[i+dx][j+dy] == '1':
                        self.union(i * M + j, (i + dx) * M + j + dy)
        res = set()
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    res.add(self.find(i * M + j))
        return len(res)

# @lc code=end

