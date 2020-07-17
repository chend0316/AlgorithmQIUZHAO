class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0: return 0
        prev, cur = 0, 1
        for i in range(n):
            cur, prev = cur + prev, cur
        return cur
