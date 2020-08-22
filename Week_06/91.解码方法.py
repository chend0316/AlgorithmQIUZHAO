#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (24.21%)
# Likes:    482
# Dislikes: 0
# Total Accepted:    63K
# Total Submissions: 259.4K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 
# 示例 1:
# 
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
# 
# 示例 2:
# 
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# 
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # if not s: return 1
        n = len(s)
        prev, cur = 0, 1

        for i in range(n):
            tmp = 0
            if s[i] in '123456789':
                tmp += cur
            # 其实一上来[i-1]会越界，但是仔细分析一下这题却没关系
            # 这只是本题的凑巧，这段DP不工整，个人不推荐这样写
            if s[i-1] == '1':
                tmp += prev
            if s[i-1] == '2' and s[i] in '0123456':
                tmp += prev
            prev, cur = cur, tmp

        return cu
# @lc code=end

