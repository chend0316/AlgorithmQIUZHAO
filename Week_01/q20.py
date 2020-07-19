# 第一遍刷
class Solution:
    def isValid(self, s: str) -> bool:
        map = { ')': '(', ']': '[', '}': '{' }
        stack = []
        for c in s:
            if c in map:
                if len(stack) == 0 or stack.pop() != map[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0

# 国际站看到，栈里面放一个假节点，就不用判断栈的长度了
class Solution(object):
    def isValid(self, s):
        stack = ['N']
        m = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in m.keys():
                if stack.pop() != m[i]:
                    return False
            else:
                stack.append(i)

        return len(stack) == 1

# 超哥视频展示了国内题解一个6行的Python
# 悟到了一些东西：
# 对于这样的结构
# if A:
#     if B:
#         pass
# else:
#     pass
# 完全可以改成这样
# if not A:
#     pass
# elif B:
#     pass

# 改进后的代码
class Solution:
    def isValid(self, s: str) -> bool:
        map = { ')': '(', ']': '[', '}': '{' }
        stack = ['#']
        for c in s:
            if c not in map: stack.append(c)
            elif stack.pop() != map[c]: return False
        return len(stack) == 1
