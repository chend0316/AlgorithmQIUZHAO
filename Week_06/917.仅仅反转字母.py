#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#
# https://leetcode-cn.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (55.90%)
# Likes:    60
# Dislikes: 0
# Total Accepted:    16.5K
# Total Submissions: 29.6K
# Testcase Example:  '"ab-cd"'
#
# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入："ab-cd"
# 输出："dc-ba"
# 
# 
# 示例 2：
# 
# 输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
# 
# 
# 示例 3：
# 
# 输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
# 
# 
# 
# 
# 提示：
# 
# 
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S 中不包含 \ or "
# 
# 
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        arr = list(S)
        i, j = 0, len(S) - 1
        while i < j:
            if not arr[i].isalpha():
                i += 1
                continue
            if not arr[j].isalpha():
                j -= 1
                continue
            arr[i], arr[j] = arr[j], arr[i]
        return ''.join(arr)

# @lc code=end
