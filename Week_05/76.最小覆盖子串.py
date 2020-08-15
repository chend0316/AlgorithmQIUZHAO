#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (38.26%)
# Likes:    692
# Dislikes: 0
# Total Accepted:    69.9K
# Total Submissions: 181.4K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。
# 
# 
# 
# 示例：
# 
# 输入：S = "ADOBECODEBANC", T = "ABC"
# 输出："BANC"
# 
# 
# 
# 提示：
# 
# 
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""
        resLen = math.inf
        res = ""
        cnt = collections.Counter(t)
        i = 0
        for j in range(len(s)):
            # s[i...j] 闭区间
            c = s[j]
            if c in cnt: cnt[c] -= 1
            while i < j and (s[i] not in cnt or cnt[s[i]] < 0):
                if s[i] in cnt: cnt[s[i]] += 1
                i += 1
            if sum([1 if e > 0 else 0 for e in cnt.values()]) == 0 and j - i + 1 < resLen:
                res = s[i:j+1]
                resLen = j - i + 1
        return res

# @lc code=end

