#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (29.95%)
# Likes:    268
# Dislikes: 0
# Total Accepted:    27.4K
# Total Submissions: 90.9K
# Testcase Example:  '2\n[2,4,1]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# 
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 示例 1:
# 
# 输入: [2,4,1], k = 2
# 输出: 2
# 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 
# 
# 示例 2:
# 
# 输入: [3,2,6,5,0,3], k = 2
# 输出: 7
# 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4
# 。
# 随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, K: int, prices: List[int]) -> int:
        N = len(prices)
        if K > N // 2: return self.greedy(prices)
        dp = [[[0]*(K+1) for _ in range(2)] for _ in range(N+1)]
        # k 约定为买入的次数
        for k in range(K+1):
            dp[-1][1][k] = -math.inf
            # dp[-1][0][k] = 0
        
        for i in range(N):
            for k in range(K+1):
                dp[i][0][k] = max(dp[i-1][0][k], dp[i-1][1][k] + prices[i])
                if k > 0:
                    dp[i][1][k] = max(dp[i-1][1][k], dp[i-1][0][k-1] - prices[i])
                else:
                    dp[i][1][k] = -math.inf
        
        return dp[N-1][0][K]
    
    def greedy(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res
# @lc code=end

