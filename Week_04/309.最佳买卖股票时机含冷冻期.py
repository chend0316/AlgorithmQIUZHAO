#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (56.76%)
# Likes:    494
# Dislikes: 0
# Total Accepted:    51.4K
# Total Submissions: 90.4K
# Testcase Example:  '[1,2,3,0,2]'
#
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
# 
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 
# 
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 
# 
# 示例:
# 
# 输入: [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
# @lc code=end

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        a = [0]*(n+2)  # 没有股票
        b = [0]*(n+2)  # 持有股票
        a[-2] = 0
        a[-1] = 0
        # b[-2] = xxx  # 不管初始化为任何值，都不影响结果
        b[-1] = -prices[0]  # 也可用负无穷大

        for i in range(n):
            a[i] = max(a[i-1], b[i-1] + prices[i])
            b[i] = max(b[i-1], a[i-2] - prices[i])
        
        return a[n-1]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        a = [0]*(n+1)  # 没有股票
        b = [0]*(n+1)  # 持有股票
        c = [0]*(n+1)  # 冷冻期
        a[-1] = 0
        b[-1] = -prices[0]  # 也可用负无穷大
        c[-1] = 0

        for i in range(n):
            a[i] = max(a[i-1], c[i-1])
            b[i] = max(b[i-1], a[i-1] - prices[i])
            c[i] = b[i-1] + prices[i]
        
        return max(a[n-1], c[n-1])