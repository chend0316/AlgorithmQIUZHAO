import collections
import heapq

# 第一遍，暴力法，O(N^2)，熟悉了deque的使用
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = collections.deque(nums[:k-1], k)
        res = []
        for num in nums[k-1:]:
            window.append(num)
            res.append(max(window))
        return res

# 后来脑子短路想维护大顶堆做这题，O(NlogN)
# 根本不能用堆，因为窗口每次弹出的元素是最左元素，而不是堆顶元素

# 看了别人的答案后
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k: return []
        res = []
        deq = collections.deque()
        for i in range(k-1):
            while len(deq) and deq[-1] < nums[i]:
                deq.pop()
            deq.append(nums[i])
        for i in range(k-1, len(nums)):
            while len(deq) and deq[-1] < nums[i]:
                deq.pop()
            deq.append(nums[i])
            res.append(deq[0])
            if nums[i-k+1] == deq[0]: deq.popleft()
        return res

# 继续看了别人的答案，优化了代码逻辑
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = collections.deque()
        res = []
        for i, num in enumerate(nums):
            while deq and nums[deq[-1]] <= num:
                deq.pop()
            deq.append(i)
            if deq[0] == i - k:
                deq.popleft()
            if i >= k - 1:
                res.append(nums[deq[0]])
        return res
