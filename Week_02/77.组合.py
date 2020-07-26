#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (74.24%)
# Likes:    320
# Dislikes: 0
# Total Accepted:    63.1K
# Total Submissions: 85K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 
# 示例:
# 
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.n = n
        self.dfs(k, 1, [])
        return self.ans
    
    def dfs(self, k, start, path):
        if k == 0:
            self.ans.append(path[:])
            return
        if start > self.n: return

        for i in range(start, self.n + 1):
            self.dfs(k - 1, i + 1, path + [i])

# @lc code=end

