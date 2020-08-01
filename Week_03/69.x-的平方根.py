#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (38.76%)
# Likes:    458
# Dislikes: 0
# Total Accepted:    181.8K
# Total Submissions: 469.2K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
# 
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 
# 示例 1:
# 
# 输入: 4
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
# 由于返回类型是整数，小数部分将被舍去。
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0: return 0
        lo, hi = 1, x
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if mid * mid < x: lo = mid
            elif x < mid * mid: hi = mid - 1
            else: return mid
        return lo

# @lc code=end
s = Solution()
print(s.mySqrt(8))

