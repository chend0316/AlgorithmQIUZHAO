#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# https://leetcode-cn.com/problems/word-ladder/description/
#
# algorithms
# Medium (42.83%)
# Likes:    380
# Dislikes: 0
# Total Accepted:    50.1K
# Total Submissions: 116.8K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
# 的最短转换序列的长度。转换需遵循如下规则：
# 
# 
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 
# 
# 说明:
# 
# 
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 
# 
# 示例 1:
# 
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# ⁠    返回它的长度 5。
# 
# 
# 示例 2:
# 
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
# 
#
from typing import *
import collections

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:


# @lc code=end

# BFS
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not wordList or endWord not in wordList: return 0
        K = len(beginWord)
        neighbors = {}
        for word in wordList + [beginWord]:  # 没必要加 beginWord?
            for i in range(K):
                key = word[:i] + '*' + word[i + 1:]
                neighbors.setdefault(key, [])
                neighbors[key].append(word)
        
        # bfs
        queue = collections.deque()
        visited = set()
        queue.append(beginWord)
        res = 0
        while queue:
            n = len(queue)
            res += 1
            while n:
                n -= 1
                word = queue.popleft()
                visited.add(word)
                if word == endWord: return res
                for i in range(K):
                    key = word[:i] + '*' + word[i + 1:]
                    for neighbor in neighbors[key]:
                        if neighbor not in visited:
                            queue.append(neighbor)
        return 0

# 双向BFS
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList: return 0
        K = len(beginWord)
        neighbors = {}
        for word in wordList + [beginWord]:
            for i in range(K):
                w = word[:i] + '*' + word[i + 1:]
                neighbors.setdefault(w, [])
                neighbors[w].append(word)

        beginSet = {beginWord,}
        endSet = {endWord,}
        res = 1
        visited = set()
        while beginSet and endSet:
            if len(beginSet) > len(endSet): beginSet, endSet = endSet, beginSet
            tmpSet = set()
            for word in beginSet:
                if word in visited: continue
                visited.add(word)
                for i in range(K):
                    w = word[:i] + '*' + word[i + 1:]
                    for neighbor in neighbors[w]:
                        if neighbor in endSet: return res + 1
                        tmpSet.add(neighbor)
            beginSet = tmpSet
            res += 1

        return 0
