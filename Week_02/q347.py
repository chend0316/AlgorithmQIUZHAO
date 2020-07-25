# 第一遍，先排序
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        sorted_count = sorted([(num, cnt) for num, cnt in count.items()], key=operator.itemgetter(1))
        return [num for num, _ in sorted_count[-k:]]

# 第一遍，用堆
# 首先对 num 计数，得到 cnt
# 要对 cnt 进行堆排序，但题目要求的是 num，所以还要保存 cnt -> num 的对应关系
from heapq import nlargest
import operator

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_cnt = {}
        for num in nums:
            num_to_cnt.setdefault(num, 0)
            num_to_cnt[num] += 1
        num_cnt_tuples = [(cnt, num) for num, cnt in num_to_cnt.items()]
        return [num for cnt, num in nlargest(k, num_cnt_tuples, key=operator.itemgetter(0))]
