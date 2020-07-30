#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (70.28%)
# Likes:    478
# Dislikes: 0
# Total Accepted:    52.1K
# Total Submissions: 74K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 
# 示例:
# 
# 输入: 4
# 输出: [
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
# 
# 
# 
# 
# 提示：
# 
# 
# 
# 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。（引用自
# 百度百科 - 皇后 ）
# 
# 
#
from typing import *

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n <= 0: return []
        self.ans = []
        self.n = n
        self.backtrace([], [], [])
        return self.ans

    def backtrace(self, qs, xy_diff, xy_sum):
        if len(qs) == self.n:
            self.ans.append(['.' * q + 'Q' + '.' * (self.n - q - 1) for q in qs])
            return
        for q in range(self.n):
            x, y = len(qs) - 1, q
            if q in qs or x + y in xy_sum or x - y in xy_diff: continue
            self.backtrace(qs + [q], xy_diff + [x - y], xy_sum + [x + y])

# @lc code=end

# 这边不开辟临时空间，让代码变得太长了
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n <= 0: return []
        self.ans = []
        self.n = n
        self.backtrace([], [], [])
        return self.ans

    def backtrace(self, qs, xy_diff, xy_sum):
        if len(qs) == self.n:
            self.ans.append(['.' * q + 'Q' + '.' * (self.n - q - 1) for q in qs])
            return
        for q in range(self.n):
            if q in qs: continue
            x, y = len(qs) - 1, q
            if x + y in xy_sum: continue
            if x - y in xy_diff: continue
            xy_diff.append(x - y)
            xy_sum.append(x + y)
            qs.append(q)
            self.backtrace(qs, xy_diff, xy_sum)
            xy_diff.pop()
            xy_sum.pop()
            qs.pop()
