#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
# https://leetcode-cn.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (38.44%)
# Likes:    215
# Dislikes: 0
# Total Accepted:    54.2K
# Total Submissions: 140.6K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 
# 
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 
# 
# 示例 1:
# 
# 输入:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# 输出: false
# 
#

# @lc code=start

# 当做搜索树
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        N, M = len(matrix), len(matrix[0])
        i, j = 0, M - 1

        while i < N and j >= 0:
            if target < matrix[i][j]: j -= 1
            elif target > matrix[i][j]: i += 1
            else: return True
        
        return False

# @lc code=end

