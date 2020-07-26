#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (59.39%)
# Likes:    357
# Dislikes: 0
# Total Accepted:    73.8K
# Total Submissions: 124.2K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 
# 示例:
# 
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
#

# @lc code=start
import collections

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.recursive(collections.Counter(nums), [])
        return self.ans

    def recursive(self, cnts, path):
        if sum(cnts.values()) == 0: self.ans.append(path)
        for num, cnt in cnts.items():
            if cnt == 0: continue
            cnts[num] -= 1
            self.recursive(cnts, path + [num])
            cnts[num] += 1

# @lc code=end

