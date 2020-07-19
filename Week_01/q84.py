# 第一遍暴力法，O(N^2)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        res = 0

        for m in range(N):
            l = r = m
            height = heights[m]
            while l >= 0 and heights[l] >= height:
                l -= 1
            while r < N and heights[r] >= height:
                r += 1
            res = max(res, (r - l - 1) * height)

        return res

# 参考题解，单调栈，todo还没转化为自己的知识
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [0]
        heights.append(0)
        n = len(heights)
        res = 0

        for i in range(n):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, w * h)
            stack.append(i)

        return res
