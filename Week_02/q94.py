# 第一遍，递归
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        ret = []
        if root.left:
            ret.extend(self.inorderTraversal(root.left))
        ret.append(root.val)
        if root.right:
            ret.extend(self.inorderTraversal(root.right))
        return ret

# 第一遍，递归
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        if root: self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if root.left: self.traverse(root.left)
        self.res.append(root.val)
        if root.right: self.traverse(root.right)
