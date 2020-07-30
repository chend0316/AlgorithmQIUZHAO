#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#
# https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (60.95%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    15K
# Total Submissions: 24.6K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# 您需要在二叉树的每一行中找到最大的值。
# 
# 示例：
# 
# 
# 输入: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \  
# ⁠     5   3   9 
# 
# 输出: [1, 3, 9]
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        queue = collections.deque()
        if root: queue.append(root)
        while queue:
            nodes = list(queue)
            queue.clear()
            res.append(max([node.val for node in nodes]))
            for node in nodes:
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res

        
# @lc code=end

