# 第一遍，先构造无向图的邻接表，然后进行BFS层次遍历
# 超时了，看了题解，应该是因为我的邻接表太大了
# 【错误邻接表】
# 'aaa' 'aab' 'aac' 'aad' 'aae' 两两组合、互为邻居，边的数量为5*4
# 【正确邻接表】引入中间状态
# 'aaa' 'aab' 'aac' 'aad' 'aae' 这5个和'aa*'做邻居，边的数量为5
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        beginIndex, endIndex = wordList.index(beginWord), wordList.index(endWord)
        graph = {}
        for word in wordList:
            graph[word] = []
        for word1 in graph:
            for word2 in wordList:
                # 这个邻接表太大了
                if self.distance(word1, word2) == 1:
                    graph[word1].append(word2)
        
        queue = [beginWord]
        visited = set([beginWord])
        level = 1
        while queue:
            # print(queue)
            if endWord in queue:
                return level
            queueSize = len(queue)
            for _ in range(queueSize):
                for neighbor in graph[queue[0]]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                queue.pop(0)
            level += 1

        return 0
    
    def distance(self, a, b):
        ret = 0
        for i in range(len(a)):
            if a[i] != b[i]: ret += 1
        return ret
