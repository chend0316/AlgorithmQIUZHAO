#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (38.29%)
# Likes:    849
# Dislikes: 0
# Total Accepted:    151.3K
# Total Submissions: 394K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 
# 你可以假设数组中不存在重复的元素。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 示例 1:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 
# 
# 示例 2:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        if len(nums) == 1 and nums[0] == target: return 0
        if len(nums) == 1: return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target: return m
            elif nums[m] > nums[left] and target > nums[m]: left = m + 1
            elif nums[m] < nums[right] and target < 
        
        return left if left == right else -1

# @lc code=end

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] < nums[-1] or len(nums) < 2: return self.binSearch(nums, 0, len(nums) - 1, target)
        lstart, rend = 0, len(nums)
        lend, rstart = 0, len(nums)
        while lend < rstart - 1:
            m = (lend + rstart) // 2
            if nums[m] > nums[lend]:
                lend = m
            else:
                rstart = m
        lidx = self.binSearch(nums, lstart, lend, target)
        ridx = self.binSearch(nums, rstart, rend, target)
        if lidx != -1: return lidx
        if ridx != -1: return ridx
        return -1

    def binSearch(self, nums, left, right, target):
        while start < end:
            m = (left + right) // 2
            if nums[m] < target:
                left = m + 1
            elif nums[m] > target:
                right = m - 1
            else:
                return m
        return -1

