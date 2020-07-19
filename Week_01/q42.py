# 第一遍
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        heighest_left = [0]*n
        heighest_right = [0]*n

        for i in range(1, n - 1):
            heighest_left[i] = max(heighest_left[i - 1], height[i - 1])
        for i in range(n - 2, 0, -1):
            heighest_right[i] = max(heighest_right[i + 1], height[i + 1])
        for i in range(1, n - 1):
            h_min = min(heighest_left[i], heighest_right[i])
            h_diff = h_min - height[i]
            if h_diff > 0: res += h_diff

        return res