class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        res = 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, (j - i) * height[i])
                i += 1
            else:
                res = max(res, (j - i) * height[j])
                j -= 1

        return res

# 然后Python没有++操作符，所以代码反而比Java长一些
