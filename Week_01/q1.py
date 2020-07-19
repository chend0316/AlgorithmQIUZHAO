class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2: return []
        dic = {}
        for i, n in enumerate(nums):
            if target - n in dic:
                return [dic[target - n], i]
            dic[n] = i
        return []