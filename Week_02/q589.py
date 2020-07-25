# 第一遍
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        ret = [root.val]
        for child in root.children:
            ret.extend(self.preorder(child))
        return ret