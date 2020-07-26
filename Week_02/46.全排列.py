#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (76.46%)
# Likes:    803
# Dislikes: 0
# Total Accepted:    158.9K
# Total Submissions: 207.5K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.recursive(nums, [])
        return self.ans
    
    def recursive(self, nums, path):
        if not nums: self.ans.append(path)
        for idx in range(len(nums)):
            num = nums.pop(idx)
            self.recursive(nums, path + [num])
            nums.insert(idx, num)


# @lc code=end

# 人生苦短，别管内存占用
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.recursive(nums, [])
        return self.ans
    
    def recursive(self, nums, path):
        if not nums: self.ans.append(path)
        for idx, num in enumerate(nums):
            # 渣男，直接生孩子，然后把孩子传给下一个接盘侠
            # 自己是爽了，但是内存占用多了
            self.recursive(nums[:idx] + nums[idx+1:], path + [num])  # 这里会生下很多nums数组

# 优化内存占用
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.recursive(nums, [])
        return self.ans
    
    def recursive(self, nums, path):
        if not nums: self.ans.append(path)
        for idx in range(len(nums)):
            num = nums.pop(idx)
            self.recursive(nums, path + [num])
            nums.insert(idx, num)
