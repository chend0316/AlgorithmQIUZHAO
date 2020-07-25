# 第一遍
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        ret = []
        for child in root.children:
            ret.extend(self.postorder(child))
        return ret + [root.val]