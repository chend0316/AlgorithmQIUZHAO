class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle: return 0
        N = len(triangle)
        dp = [0] * (N + 1)

        for level in range(N-1, -1, -1):
            for i in range(level + 1):
                dp[i] = min(dp[i], dp[i + 1]) + triangle[level][i]
        
        return dp[0]

# 在国际站发现Python的好东西，其它语言目测做不到
# 改进前：for j in range(N-1, -1, -1):
# 改进后：for row in triangle[::-1]:
