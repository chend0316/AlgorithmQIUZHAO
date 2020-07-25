# 第一遍
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k]

# 第一遍
from heapq import heapify, heappop
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        res = []
        heapify(arr)
        for _ in range(k):
            res.append(heappop(arr))
        return res
