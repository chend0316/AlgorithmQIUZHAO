#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#
# https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (71.40%)
# Likes:    215
# Dislikes: 0
# Total Accepted:    71.7K
# Total Submissions: 100.2K
# Testcase Example:  `"Let's take LeetCode contest"`
#
# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
# 
# 
# 
# 示例：
# 
# 输入："Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
# 
# 
# 
# 
# 提示：
# 
# 
# 在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
# 
# 
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        i, n = 0, len(s)
        stack = []
        while i < n:
            if s[i] == ' ':
                res.extend(reversed(stack))
                res.append(' ')
                stack = []
            else:
                stack.append(s[i])
            i += 1
        res.extend(reversed(stack))
        return ''.join(res)
        
# @lc code=end

