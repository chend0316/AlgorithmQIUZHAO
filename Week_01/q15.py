class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3: return []
        N = len(nums)
        res = []
        nums.sort()

        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]: continue
            j, k = i + 1, N - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                    # 我自己一直以为这边需要再加一个循环跳过重复的，发现老外都没加，悟到是多余的
                    # while j < k and nums[j] == nums[j - 1]: j += 1
                elif s > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1; k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
        
        return res
