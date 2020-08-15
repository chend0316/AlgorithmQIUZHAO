#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (75.76%)
# Likes:    1188
# Dislikes: 0
# Total Accepted:    153.8K
# Total Submissions: 202.7K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例：
# 
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
# 
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.backtrack(n, n, '')
        return self.ans
    
    def backtrack(self, left, right, path):
        if right < left or left < 0 or right < 0: return
        if left + right == 0:
            self.ans.append(path)
            return
        self.backtrack(left - 1, right, path + '(')
        self.backtrack(left, right - 1, path + ')')
       
# @lc code=end
