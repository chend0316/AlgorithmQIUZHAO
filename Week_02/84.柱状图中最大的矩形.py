#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (41.13%)
# Likes:    800
# Dislikes: 0
# Total Accepted:    72.2K
# Total Submissions: 175.3K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
# 
# 
# 
# 
# 
# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
# 
# 
# 
# 
# 
# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
# 
# 
# 
# 示例:
# 
# 输入: [2,1,5,6,2,3]
# 输出: 10
# 
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        height_stack = [0]
        idx_stack = [-1]
        res = 0
        for i, h in enumerate(heights):
            while height_stack and height_stack[-1] > h:
                idx_stack.pop()
                res = max(res, height_stack.pop() * (i - idx_stack[-1] - 1)) 
            height_stack.append(h)
            idx_stack.append(i)
        return res

# @lc code=end
