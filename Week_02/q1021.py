# 第一遍刷
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = []
        level = 0
        for c in S:
            if c == '(': level += 1
            else: level -= 1
            if level > 1 or (level == 1 and c == ')'):
                res.append(c)
        return ''.join(res)