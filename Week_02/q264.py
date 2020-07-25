# 第一遍，暴力，自己知道会超时，只是先随便写出来看看
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 0: return 0
        res = 1
        cur_num = 2
        for _ in range(n - 1):
            while True:
                x = cur_num
                while x > 1 and x % 2 == 0: x //= 2
                while x > 1 and x % 3 == 0: x //= 3
                while x > 1 and x % 5 == 0: x //= 5
                if x == 1:
                    res = cur_num
                    cur_num += 1
                    break
                cur_num += 1
        return res

# 第一遍，动态规划
# 假设 a 是丑数，那么 a/2 a/3 a/5 三个有一个也是丑数
# 所以这里用自顶向下的DP，可能不算严格的DP，但思想是一样的：缓存重复子问题的解
# 但这里还是会超时，因为仍然有暴力的成分在
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 0: return 0
        dp = set([1, 2, 3, 5])  # 虽然这里是DP
        ret = x = 0
        for _ in range(n):
            while True:
                x += 1  # 但这里仍然是暴力
                if x in dp: break
                if (x % 2 == 0 and x // 2 in dp or
                    x % 3 == 0 and x // 3 in dp or 
                    x % 5 == 0 and x // 5 in dp):
                    dp.add(x)
                    break
            ret = x

        return ret

# 新的数一定是由旧的数通过 *2 *3 *5 得到的，然而这里有顺序的问题不好搞（要用数论知识？），直接去看题解了

# 题解：用堆


# 题解：用DP，原来是用3个指针确定DP的顺序，妙啊！自己确实没有想到
# 但是这题3个指针并不是每次只有1个指针++，最多可能3个指针都++，因为3个指针有可能重复的（需要一些数论的敏感度）
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0: return 0
        ugly_nums = [1]
        prime_nums = [2, 3, 5]
        idx = [0, 0, 0]
        K = 3
        for _ in range(n - 1):
            candidate_nums = [prime_nums[i] * ugly_nums[idx[i]] for i in range(K)]
            candidate_min = min(candidate_nums)
            ugly_nums.append(candidate_min)
            for i in range(K):
                if candidate_nums[i] == candidate_min:
                    idx[i] += 1
        return ugly_nums[-1]
