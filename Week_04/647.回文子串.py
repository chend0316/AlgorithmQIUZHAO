#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#
# https://leetcode-cn.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (61.97%)
# Likes:    295
# Dislikes: 0
# Total Accepted:    35.5K
# Total Submissions: 56.9K
# Testcase Example:  '"abc"'
#
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
# 
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
# 
# 示例 1:
# 
# 
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".
# 
# 
# 示例 2:
# 
# 
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 注意:
# 
# 
# 输入的字符串长度不会超过1000。
# 
# 
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s: return 0
        N = len(s)
        res = 0
        dp = [[0]*N for _ in range(N)]
        # dp[i][j] 表示s[i...j]是否为回文串
        # 约定 i 必须小于 j
        for i in range(N-1, -1, -1):
            for j in range(N-1, -1, -1):
                if i > j: continue
                elif i == j: dp[i][j] = 1
                elif i == j - 1: dp[i][j] = 1 if s[i] == s[j] else 0
                else: dp[i][j] = dp[i+1][j-1] if s[i] == s[j] else 0
                res += dp[i][j]
        return res

# @lc code=end

