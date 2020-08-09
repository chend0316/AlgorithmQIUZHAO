#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
# https://leetcode-cn.com/problems/maximal-square/description/
#
# algorithms
# Medium (42.50%)
# Likes:    505
# Dislikes: 0
# Total Accepted:    65.6K
# Total Submissions: 153.7K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
# 
# 示例:
# 
# 输入: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# 输出: 4
# 
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        N, M = len(matrix), len(matrix[0])
        dp = [[0]*(M+1) for _ in range(N+1)]
        res = 0

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 0
                res = max(res, dp[i][j] ** 2)

        return res

# @lc code=end

