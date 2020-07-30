#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#
# https://leetcode-cn.com/problems/minimum-genetic-mutation/description/
#
# algorithms
# Medium (51.06%)
# Likes:    42
# Dislikes: 0
# Total Accepted:    6.4K
# Total Submissions: 12.5K
# Testcase Example:  '"AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]'
#
# 一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。
# 
# 假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
# 
# 例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。
# 
# 与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。
# 
# 现在给定3个参数 — start, end,
# bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。
# 
# 注意:
# 
# 
# 起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
# 所有的目标基因序列必须是合法的。
# 假定起始基因序列与目标基因序列是不一样的。
# 
# 
# 示例 1:
# 
# 
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
# 
# 返回值: 1
# 
# 
# 示例 2:
# 
# 
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# 
# 返回值: 2
# 
# 
# 示例 3:
# 
# 
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# 
# 返回值: 3
# 
# 
#
from typing import *
import collections

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
                

# @lc code=end
# 暴力广搜
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        res = 0
        visited = set()
        queue = collections.deque()
        queue.append(start)

        while queue:
            n = len(queue)
            while n:
                n -= 1
                node = queue.popleft()
                visited.add(node)
                if node == end: return res
                for neighbor in self.neighbors(node):
                    if neighbor not in visited and neighbor in bank:
                        queue.append(neighbor)
            res += 1

        return -1
    
    def neighbors(self, node):
        ret = []
        for i in range(len(node)):
            for c in 'ACGT':
                if node[i] == c: continue
                ret.append(node[:i] + c + node[i + 1:])
        return ret

# 先构造邻接表，然后暴力广搜
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        graph = self.genGraph([start] + bank)
        res = 0
        visited = set()
        queue = collections.deque()
        queue.append(start)

        while queue:
            n = len(queue)
            while n:
                n -= 1
                node = queue.popleft()
                visited.add(node)
                if node == end: return res
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            res += 1

        return -1

    def genGraph(self, bank):
        ret = {}
        n = len(bank)
        for b in bank:
            ret[b] = []
        for i in range(n):
            for j in range(i + 1, n):
                if self.distance(bank[i], bank[j]) == 1:
                    ret[bank[i]].append(bank[j])
                    ret[bank[j]].append(bank[i])
        return ret

    def distance(self, s1, s2):
        ret = 0
        for (c1, c2) in zip(s1, s2):
            if c1 != c2: ret += 1
        return ret



s = Solution()
res = s.minMutation(
    "AAAAAAAA",
    "CCCCCCCC",
    ["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA"]
)
print(res)
