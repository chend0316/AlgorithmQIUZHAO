# 第一遍
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        n = len(nums)
        k = k % n
        for i in range(k):
            nums.insert(0, nums.pop())
