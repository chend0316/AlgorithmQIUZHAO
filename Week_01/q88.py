# 第一遍
# 这题其实很简单，但代码细节翻车了（当nums1为空的情况没考虑）
# 果断看题解了，看完题解后的代码如下
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p2 >= 0 and p1 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p, p2 = p - 1, p2 - 1

# Python的这个语法，妙啊
nums1[:p2+1] = nums2[:p2+1]
