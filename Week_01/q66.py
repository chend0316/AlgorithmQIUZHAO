# 第一遍
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = digits[:]

        for i in range(len(res) - 1, -1, -1):
            res[i] = (res[i] + 1) % 10
            if res[i] != 0:
                return res

        return [1] + res
