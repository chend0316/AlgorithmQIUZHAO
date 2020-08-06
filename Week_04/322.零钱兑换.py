#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (40.39%)
# Likes:    727
# Dislikes: 0
# Total Accepted:    113.6K
# Total Submissions: 279.4K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 
# 
# 
# 示例 1:
# 
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1
# 
# 示例 2:
# 
# 输入: coins = [2], amount = 3
# 输出: -1
# 
# 
# 
# 说明:
# 你可以认为每种硬币的数量是无限的。
# 
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        dp = [0]*(n+1)
        for i in range(1, n + 1):
            minSteps = n + 1
            for j in coins:
                if i - j >= 0:
                    minSteps = min(minSteps, dp[i - j] + 1)
            dp[i] = minSteps
        return dp[n] if dp[n] != n + 1 else -1

        
# @lc code=end

