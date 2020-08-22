#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#
# https://leetcode-cn.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (31.19%)
# Likes:    500
# Dislikes: 0
# Total Accepted:    50.8K
# Total Submissions: 162.7K
# Testcase Example:  '"aa"\n"a"'
#
# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
# 
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 
# 
# 两个字符串完全匹配才算匹配成功。
# 
# 说明:
# 
# 
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
# 
# 
# 示例 1:
# 
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 
# 示例 2:
# 
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
# 
# 
# 示例 3:
# 
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 
# 
# 示例 4:
# 
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
# 
# 
# 示例 5:
# 
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输出: false
# 
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[None]*(m+1) for _ in range(n+1)]
        for i in range(-1, n):
            for j in range(-1, m):
                if i == -1 and j == -1: dp[i][j] = True
                elif j == -1: dp[i][j] = False
                elif i == -1:
                    if p[j] == '*': dp[i][j] = dp[i][j-1]
                    else: dp[i][j] = False
                else:
                    if p[j] == '?': dp[i][j] = dp[i-1][j-1]
                    elif p[j] == '*': dp[i][j] = dp[i-1][j] or dp[i][j-1]
                    else: dp[i][j] = s[i] == p[j] and dp[i-1][j-1]
        return dp[n-1][m-1]

# @lc code=end

class Solution:
    def __init__(self):
        self.memo = {}

    def isMatch(self, s: str, p: str) -> bool:
        if (s, p) in self.memo: return self.memo[(s, p)]
        self.memo[(s, p)] = self._isMatch(s, p)
        return self.memo[(s, p)]

    def _isMatch(self, s: str, p: str) -> bool:
        if not s:
            if not p: return True
            if p[0] == '*': return self.isMatch(s, p[1:])
            else: return False
        if not p: return False
        if p[0] == '?': return self.isMatch(s[1:], p[1:])
        if p[0] == '*': return self.isMatch(s[1:], p) or self.isMatch(s, p[1:])
        return s[0] == p[0] and self.isMatch(s[1:], p[1:])
