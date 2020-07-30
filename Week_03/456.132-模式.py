#
# @lc app=leetcode.cn id=456 lang=python3
#
# [456] 132模式
#
# https://leetcode-cn.com/problems/132-pattern/description/
#
# algorithms
# Medium (27.34%)
# Likes:    185
# Dislikes: 0
# Total Accepted:    10.3K
# Total Submissions: 37.5K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak <
# aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
# 
# 注意：n 的值小于15000。
# 
# 示例1:
# 
# 
# 输入: [1, 2, 3, 4]
# 
# 输出: False
# 
# 解释: 序列中不存在132模式的子序列。
# 
# 
# 示例 2:
# 
# 
# 输入: [3, 1, 4, 2]
# 
# 输出: True
# 
# 解释: 序列中有 1 个132模式的子序列： [1, 4, 2].
# 
# 
# 示例 3:
# 
# 
# 输入: [-1, 3, 2, 0]
# 
# 输出: True
# 
# 解释: 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].
# 
# 
#
import math
from typing import *

# @lc code=start
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3: return False
        max1 = nums[-1]
        max2 = -math.inf

        for num in reversed(nums[:-1]):
            print(num, max1, max2)
            if num < max2: return True
            if num > max1: max1, max2 = num, max1
        
        return False

# @lc code=end

s = Solution()
# print(s.find132pattern([1,2,3,4]))
# print(s.find132pattern([1,2,3,2]))
# print(s.find132pattern([1,2,3]))
# print(s.find132pattern([0,2,1]))
# print(s.find132pattern([0,2,0]))
# print(s.find132pattern([0,2,2]))
print(s.find132pattern([-2,1,2,-2,1,2]))
