#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#
# https://leetcode-cn.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (54.49%)
# Likes:    87
# Dislikes: 0
# Total Accepted:    19.6K
# Total Submissions: 35.8K
# Testcase Example:  '"abcdefg"\n2'
#
# 给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。
# 
# 
# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
# 
# 
# 
# 
# 示例:
# 
# 输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"
# 
# 
# 
# 
# 提示：
# 
# 
# 该字符串只包含小写英文字母。
# 给定字符串的长度和 k 在 [1, 10000] 范围内。
# 
# 
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        i, n = 0, len(s)
        while i < n:
            j = 0
            stack = []
            while i < n and j < k:
                stack.append(s[i])
                i += 1; j += 1
            res.extend(reversed(stack))
            queue = []
            while i < n and j < 2 * k:
                queue.append(s[i])
                i += 1; j += 1
            res.extend(queue)
        return ''.join(res)

# @lc code=end

