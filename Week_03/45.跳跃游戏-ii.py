#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# https://leetcode-cn.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (36.92%)
# Likes:    643
# Dislikes: 0
# Total Accepted:    73.6K
# Total Submissions: 198.3K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
# 
# 示例:
# 
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 
# 
# 说明:
# 
# 假设你总是可以到达数组的最后一个位置。
# 
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
# @lc code=end

# 方法一，超时
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [math.inf] * n
        ans[0] = 0

        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    ans[i + j] = min(ans[i + j], ans[i] + 1)

        return ans[-1]

# 方法二，成批更新 maxRange 有点像按层次遍历
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxRange = 0
        res = 0
        i = 0

        while maxRange < n - 1:
            newMaxRange = maxRange
            while i <= maxRange:
                newMaxRange = max(newMaxRange, i + nums[i])
                i += 1
            res += 1
            maxRange = newMaxRange

        return res
