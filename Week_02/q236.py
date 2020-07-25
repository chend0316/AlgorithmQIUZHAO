# 第一遍
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        if root: self.traverse(root, p, q)
        return self.ans

    def traverse(self, root, p, q):
        l = r = False
        if root.left: l = self.traverse(root.left, p, q)
        if root.right: r = self.traverse(root.right, p, q)

        if l and r: self.ans = root
        if (root == p or root == q) and (l or r): self.ans = root

        return root == p or root == q or l or r

# 参考国际站
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        elif not right:
            return left
        else:
            return root
