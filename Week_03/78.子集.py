#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (77.61%)
# Likes:    673
# Dislikes: 0
# Total Accepted:    111.3K
# Total Submissions: 143.3K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
from typing import *

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res.extend([tmp + [num] for tmp in res])
        return res
# @lc code=end

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        picks = []
        def dfs(level):
            if level == n:
                res.append(picks[:])
                return
            dfs(level + 1)
            picks.append(nums[level])
            dfs(level + 1)
            picks.pop()
        dfs(0)
        return res
