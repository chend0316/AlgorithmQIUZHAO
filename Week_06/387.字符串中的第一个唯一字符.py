#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (46.30%)
# Likes:    254
# Dislikes: 0
# Total Accepted:    94.6K
# Total Submissions: 203.4K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 
# 
# 
# 示例：
# 
# s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
# 
# 
# 
# 
# 提示：你可以假定该字符串只包含小写字母。
# 
#

import collections

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        chr2idx = {}
        cnt = collections.defaultdict(int)
        for i in range(len(s)):
            chr2idx[s[i]] = i
            cnt[s[i]] += 1
        for k, v in cnt.items():
            if v == 1: return chr2idx[k]
        return -1

# @lc code=end

