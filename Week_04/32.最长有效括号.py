#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (33.18%)
# Likes:    891
# Dislikes: 0
# Total Accepted:    92.4K
# Total Submissions: 276.3K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# 
# 示例 1:
# 
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 
# 
# 示例 2:
# 
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 
# 
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        N = len(s)
        res = 0
        dp = [0]*N
        for i in range(N):
            if s[i] == ')':
                if i > 0 and s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2
                    if i - dp[i-1] - 2 >= 0:
                        dp[i] += dp[i-dp[i-1]-2]
            res = max(res, dp[i])
        return res
# @lc code=end

