# 第一遍，Python大法好！
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = collections.Counter(s)
        t_cnt = collections.Counter(t)
        return s_cnt == t_cnt

# 第一遍，不用库函数，自己计数
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = {}
        for c in s:
            cnt.setdefault(c, 0)
            cnt[c] += 1
        for c in t:
            if c not in cnt or cnt[c] == 0: return False
            cnt[c] -= 1
        return sum(cnt.values()) == 0

