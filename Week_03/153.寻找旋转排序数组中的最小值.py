#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (51.09%)
# Likes:    226
# Dislikes: 0
# Total Accepted:    67.1K
# Total Submissions: 130.2K
# Testcase Example:  '[3,4,5,1,2]'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] )。
# 
# 请找出其中最小的元素。
# 
# 你可以假设数组中不存在重复元素。
# 
# 示例 1:
# 
# 输入: [3,4,5,1,2]
# 输出: 1
# 
# 示例 2:
# 
# 输入: [4,5,6,7,0,1,2]
# 输出: 0
# 
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return 0
        lo, hi = 0, len(nums) - 1
        # 被旋转
        # 3 4[ 1
        # 3 1] 2
        # 没被旋转
        # 1 ]2 3
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]: lo = mid + 1
            elif nums[lo] > nums[mid]: hi = mid
            else: hi = mid - 1
        return nums[lo]
# @lc code=end

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return 0
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]: lo = mid + 1
            else: hi = mid
        return nums[lo]
