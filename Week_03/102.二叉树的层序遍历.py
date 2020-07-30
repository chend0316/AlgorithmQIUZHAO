#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (63.06%)
# Likes:    575
# Dislikes: 0
# Total Accepted:    167.9K
# Total Submissions: 266K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 
# 
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.ans = []
        self.dfs(root, 0)
        return self.ans

    def dfs(self, root, level):
        if not root: return
        if len(self.ans) <= level: self.ans.append([])
        self.ans[level].append(root.val)
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)

# @lc code=end
# BFS解法
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = collections.deque()
        if root: queue.append(root)
        while queue:
            res.append([])
            n = len(queue)
            while n:
                n -= 1
                node = queue.popleft()
                res[-1].append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return res

# DFS解法
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.ans = []
        self.dfs(root, 0)
        return self.ans

    def dfs(self, root, level):
        if not root: return
        if len(self.ans) <= level: self.ans.append([])
        self.ans[level].append(root.val)
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)
