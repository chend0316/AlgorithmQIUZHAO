#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#
# https://leetcode-cn.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (38.38%)
# Likes:    299
# Dislikes: 0
# Total Accepted:    21.6K
# Total Submissions: 56K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord
# 的最短转换序列。转换需遵循如下规则：
# 
# 
# 每次转换只能改变一个字母。
# 转换后得到的单词必须是字典中的单词。
# 
# 
# 说明:
# 
# 
# 如果不存在这样的转换序列，返回一个空列表。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 
# 
# 示例 1:
# 
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
# 
# 
# 示例 2:
# 
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: []
# 
# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
# 
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
# @lc code=end

# 方法一：队列里面放 path，因为要输出所有路径无法使用 visited，所以超时了
# 其实是可以用 visited 的，见其它方法
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not wordList or endWord not in wordList: return []
        res = []
        neighbors = {}
        K = len(beginWord)
        for word in wordList + [beginWord]:
            for i in range(K):
                key = word[:i] + '*' + word[i + 1:]
                neighbors.setdefault(key, [])
                neighbors[key].append(word)

        queue = collections.deque()
        queue.append([beginWord])
        while queue:
            found = False
            n = len(queue)
            while n:
                n -= 1
                path = queue.popleft()
                word = path[-1]
                for i in range(K):
                    key = word[:i] + '*' + word[i + 1:]
                    for neighbor in neighbors[key]:
                        if neighbor == endWord:
                            found = True
                            res.append(path + [endWord])
                        elif neighbor not in path:  # 这里要优化
                            queue.append(path + [neighbor])
            if found: break

        return res

# 方法二：队列里面放 path，然后使用 visited 确保不会走垃圾路径导致超时
# 这里的技巧是用了内外两个 visited 集合，让 visited 按层更新，而不是按次更新
# 如果是按次更新，则同层节点会冲突，导致漏解
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not wordList or endWord not in wordList: return []
        res = []
        neighbors = {}
        K = len(beginWord)
        for word in wordList + [beginWord]:
            for i in range(K):
                key = word[:i] + '*' + word[i + 1:]
                neighbors.setdefault(key, [])
                neighbors[key].append(word)

        queue = collections.deque()
        queue.append([beginWord])
        visited = { beginWord, }
        while queue:
            willVisited = set()
            found = False
            n = len(queue)
            while n:
                n -= 1
                path = queue.popleft()
                word = path[-1]
                for i in range(K):
                    key = word[:i] + '*' + word[i + 1:]
                    for neighbor in neighbors[key]:
                        if neighbor == endWord:
                            found = True
                            res.append(path + [endWord])
                        elif neighbor not in visited:  # 不能走回到上一层走过的节点
                            queue.append(path + [neighbor])
                            willVisited.add(neighbor)  # 不要写成 visited，否则就变成按次更新
            visited = visited.union(willVisited)  # 按层批量更新
            if found: break

        return res

# 方法三：队列里面放节点，而不是路径，所以这是「传统 DFS + visited」，因此自然不会走垃圾路径导致超时
# 但如何输出所有路径呢？这就是妙的地方了，见代码
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not wordList or endWord not in wordList: return []
        neighbors = {}
        K = len(beginWord)
        for word in wordList + [beginWord]:
            for i in range(K):
                key = word[:i] + '*' + word[i + 1:]
                neighbors.setdefault(key, [])
                neighbors[key].append(word)

        queue = collections.deque()
        queue.append(beginWord)
        ans = { beginWord: [[beginWord]] }
        visited = { beginWord, }
        while queue:
            if endWord in ans.keys(): break
            n = len(queue)
            willVisited = set()
            while n:
                n -= 1
                word = queue.popleft()
                for i in range(K):
                    key = word[:i] + '*' + word[i + 1:]
                    for neighbor in neighbors[key]:
                        if neighbor not in visited:
                            if neighbor not in willVisited: queue.append(neighbor)
                            willVisited.add(neighbor)
                            ans.setdefault(neighbor, [])
                            ans[neighbor].extend([t + [neighbor] for t in ans[word]])
            visited = visited.union(willVisited)

        return ans[endWord] if endWord in ans.keys() else []
