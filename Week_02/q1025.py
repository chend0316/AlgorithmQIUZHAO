# 第一遍，自己没怎么思考，直接看题解的
# 虽然直接一行代码判断奇偶就可以输出答案了
# 但是为了锻炼到自己，我还是老老实实递推了
class Solution:
    def divisorGame(self, N: int) -> bool:
        if N <= 1: return False
        res = [False] * (N + 1)
        res[2] = True
        for n in range(3, N + 1):
            for x in range(1, n):
                if n % x == 0 and not res[n - x]:
                    res[n] = True
        return res[N]
