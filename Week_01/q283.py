# 第一遍自己想的解法，把非0填到前面，最后剩余部分补0
class Solution:
    def moveZeroes(self, nums):
        i = j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1
        while i < len(nums):
            nums[i] = 0
            i += 1

# 看国际站有人的解法是用交换元素
def moveZeroes(self, nums):
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1

# 第二遍自己的解法
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        while i < len(nums):
            nums[i] = 0
            i += 1
