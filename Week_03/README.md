## 学习笔记

切题四件套（覃超老师）：

- 题目先理解清楚，和面试官沟通题目条件
- 先把所有解法都在脑海过一遍，和面试官确认所有解法和复杂度
- 和面试官确定一个解法后开始写代码
- 测试样例

五毒神掌（覃超老师）：

- 第一遍：五分钟读题思考，有思路就直接写，没思路就直接看题解并默写题解
- 第二遍：不看题解，自己写代码
- 第三遍：24小时后
- 第四遍：一周后
- 第五遍：面试前

学习方法建议和误区（自己总结的）：

- 不要在同一道题上一直研究，就像同一个汉字看多了就会不认识，同一道题一直研究“神经会疲劳”，这时候要换换题目换换脑子，过几个小时再来研究
- 不要追求完美主义，做笔记不要把所有解法都记下来，只记自己目前领悟最深的就行
- 好记性不如烂笔头，烂笔头不如谷歌；与其辛苦做所谓的大而全的笔记，不如多逛逛力扣国际站、多用谷歌搜别人的笔记总结
- 精神不振不要硬钢，注意休息、换换头脑

## 刷题笔记

### 树和图的遍历
#### DFS、BFS
- [102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)，除了用BFS竟然还能用DFS做
- [104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)
- [111. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)
- [22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)，看起来不像，但其实是DFS+剪枝
- [36. 有效的数独](https://leetcode-cn.com/problems/valid-sudoku/)
- [37. 解数独](https://leetcode-cn.com/problems/sudoku-solver/)

#### 层次遍历 vs BFS
在网上搜了一下，BFS 和层次遍历好像是同一个东西？但在我的笔记中，把他们视为不同的算法。

BFS 不能将不同层的节点“分隔”开来，层次遍历在 BFS 代码的基础上增加了一些小技巧，使得我们可以“分隔”不同层的节点。

层次遍历的基础题见[102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)，有多种实现技巧。我了解的有两种，我给他们起名字为：队列计数法、新旧队列法。

102题使用「队列计数法」的代码如下：
```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = collections.deque()
        if root: queue.append(root)
        while queue:
            res.append([])
            n = len(queue)  # 技巧
            while n:  # 技巧
                n -= 1  # 技巧
                node = queue.popleft()
                res[-1].append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res
```

102题使用「新旧队列法」的代码如下：
```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = []
        if root: queue.append(root)
        while queue:
            res.append([])
            newQueue = []  # 技巧
            for node in queue:
                res[-1].append(node.val)
                if node.left: newQueue.append(node.left)  # 技巧
                if node.right: newQueue.append(node.right)  # 技巧
            queue = newQueue  # 技巧
        return res
```

层次遍历是一个代码技巧，熟悉其思想可以写出其它变种，例如[126. 单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii/)在国际站上有[一个绝妙的解法](https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer)，就是将「新旧队列法」运用到了出神入化的地步，代码如下：

```python
# 这个例子放在这边有点太难了，因为这个老外用的技巧有点多，todo：之后找个更适合新手学习的例子吧
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)  # 用哈希表而不是队列
            for w in layer:
                if w == endWord: 
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww]+=[j+[neww] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer  # 用「新旧队列」法实现的层次遍历，不过这里用哈希表取代队列

        return res
```

#### 暴力DFS
[543. 二叉树的直径](https://leetcode-cn.com/problems/diameter-of-binary-tree/)除了暴力 DFS 还有更好的解法。

[437. 路径总和 III](https://leetcode-cn.com/problems/path-sum-iii/)有更好的解法，这里我们给出的是暴力 DFS 的代码：

```java
public class Solution {
    public int pathSum(TreeNode root, int sum) {
        if (root == null) return 0;
        return pathSumFrom(root, sum) + pathSum(root.left, sum) + pathSum(root.right, sum);
    }

    private int pathSumFrom(TreeNode node, int sum) {
        if (node == null) return 0;
        int ret = 0;
        if (node.val == sum) ret++;
        return ret + pathSumFrom(node.left, sum - node.val) + pathSumFrom(node.right, sum - node.val);
    }
}
```

[1367. 二叉树中的列表](https://leetcode-cn.com/problems/linked-list-in-binary-tree/)也能用[DP来解](https://leetcode.com/problems/linked-list-in-binary-tree/discuss/524881/Python-Recursive-Solution-O(N)-Time)，这里我们给出的是暴力 DFS 的代码：

```python
def isSubPath(self, head, root):
    def dfs(head, root):
        if not head: return True
        if not root: return False
        if root.val != head.val: return False
        return dfs(head.next, root.left) or dfs(head.next, root.right)
    if not head: return True
    if not root: return False
    # 重点学习下面这行
    return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
```

### 二分查找

千万不要小瞧二分查找，面试前重点准备，二分查找和链表都很容易丢分。二分查找有各种变形，以至于没有统一的二分模板。

为了后续介绍的统一，这里规定一些背景知识，高亮的部分都可能是二分算法的“变形点”：
- 代码变量命名为：lo、hi、mid，三个变量都是代表数组下标
- 在 \[lo, ..., hi\] 闭区间内搜索，这个区间统一叫做搜索区间
- 根据 `mid 信息`将搜索区间缩小为`左子区间`或`右子区间`
- 如果`搜索区间太小了`就退出循环
- `一定能找到目标吗`

最传统的二分代码模板如下，大家先对传统模板有个共识，熟悉了传统模板之后我们来讲二分的各种变种。
```python
def binSearch(nums, target):
    lo, hi = 0, N - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] < target: lo = mid + 1
        elif nums[mid] > target: hi = mid - 1
        else: return mid  # 找到了
    return -1  # 没找到
```

#### 变形1：左右区间是否包含 mid 呢？
「不包含mid (经典)」如果左右子区间都不包含 mid，代码为：
- `mid = (lo + hi) // 2` 可以用下取整
- `mid = (lo + hi + 1) // 2` 也可以用上取整
- `lo = mid + 1`
- `hi = mid - 1`

「右包含mid (变种)」如果右子区间包含 mid，代码为：
- `mid = (lo + hi) // 2` 不可以用下取整，会死循环
- `mid = (lo + hi + 1) // 2` 可以用上取整
- `lo = mid`
- `hi = mid - 1`

「左包含mid (变种)」如果左子区间包含 mid，代码为：
- `mid = (lo + hi) // 2` 可以用下取整
- `mid = (lo + hi + 1) // 2` 不可以用上取整，会死循环
- `lo = mid + 1`
- `hi = mid`

「全包含mid (变种)」左右子区间都可能包含 mid，无解，一定会死循环。需要借助「变形2」的知识点避免死循环：
- `mid = (lo + hi) // 2` 不可以，会死循环
- `mid = (lo + hi + 1) // 2` 不可以，会死循环
- `lo = mid + 1`
- `hi = mid - 1`

为什么会死循环呢？下面代码演示的是「右包含mid」的一个错误例子，对应题目是[69. x 的平方根](https://leetcode-cn.com/problems/sqrtx/)。如果 mid 采用下取整则可能和 lo 重合，反之采用上取整可能和 hi 重合。
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo < hi:  # 当 lo == 2 而且 hi == 3 的时候
            mid = (lo + hi) // 2  # mid 向下取整，mid == 2
            if mid * mid < x: lo = mid  # 这时候 lo 又回到 2！死循环！
            elif mid * mid > x: hi = mid - 1
            else: return mid
        return lo
```

「不包含mid」的题目有：[367. 有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square/)等等。
367题的代码如下。
```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 1: return False
        lo, hi = 1, num
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid < num: lo = mid + 1  # mid 打入冷宫
            elif mid * mid > num: hi = mid - 1  # mid 打入冷宫
            else: return True
        return False
```

「右包含mid」的题目有：[69. x 的平方根](https://leetcode-cn.com/problems/sqrtx/)等等。
69题的代码如下：
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if mid * mid < x: lo = mid  # 再给 mid 一个机会吧！
            elif mid * mid > x: hi = mid - 1
            else: return mid
        return lo
```

「左包含mid」的题目有：[278. 第一个错误的版本](https://leetcode-cn.com/problems/first-bad-version/)等等。
278题的代码如下：
```python
class Solution:
    def firstBadVersion(self, n):
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid): hi = mid  # 再给 mid 一个机会吧！
            else: lo = mid + 1
        return lo
```

#### 变形2：搜索区间多小的时候退出循环呢？
有3种情况：
- `while lo <= hi`，区间「长度为0」的时候退出
- `while lo < hi`，区间「长度为1」的时候退出
- `while lo < hi - 1`，区间「长度为2」的时候退出

区间「长度为0」的代码，用于可能无解的题型，循环退出后就返回无解。这是最经典最简单的题型。todo：也找个例题吧？

区间「长度为1」的代码用于一定有解的题型，当区间长度为1的时候，解已经明确了，就可以停止循环了。
如果你不退出循环，轻则逻辑混乱，重则死循环，请看[278. 第一个错误的版本](https://leetcode-cn.com/problems/first-bad-version/)的一个反面教材：
```python
# 这种题为啥会死循环
# 因为这题 while 内不能写 return 语句
class Solution:
    def firstBadVersion(self, n):
        lo, hi = 1, n
        while lo <= hi:  # 用 <= 会引起死循环，需要改为 <
            mid = (lo + hi) // 2
            if isBadVersion(mid): hi = mid
            else: lo = mid + 1
        return lo
```

区间「长度为2」的代码用于保证区间长度不小于3，避免「全包含mid」出现死循环。有没有这种题目呢？todo: 应该是有的，我找到了会贴在这边。

#### 变形3：如何根据 mid 信息缩小搜索区间呢？
这种变形就很灵活了，需要具体题目具体分析，没有一个通用的模板。

二分查找变种：旋转排序数组。如果有重复元素，那么会难很多。
- [33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)
- [81. 搜索旋转排序数组 II](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/)
- [153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)
- [154. 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/)

二分查找变种：搜索二维矩阵。这题可以不用二分，把矩阵当成搜索树从右上角开始搜，代码会超级简单。但出于练习目的，建议用二分来刷。
- [74. 搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)，
- [240. 搜索二维矩阵 II](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/)，二分不是这题的最优解

## 每周课内遍数记录

### week1刷题遍数记录
课内实战
| 敲代码 | 阅读别人代码 | 备注       | 题目                                                         |
| ---- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 3 |     | 暴力、双指针  | [11. 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/) |
| 3 |     |               | [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/) |
| 3 | 1   |               | [15. 三数之和](https://leetcode-cn.com/problems/3sum/)       |
| 3 | 1   |                  | [206. 反转链表](https://leetcode-cn.com/problems/reverse-linked-list/) |
| 3 | 1   | 递归、迭代、多练习   | [24. 两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/) |
| 2 | 1   | 哈希表、快慢指针 | [141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/) |
| 1 | \*2 | 哈希表、\*快慢指针 | [\*142. 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/) |
| 1 | \*1 |                  | [25. K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/) |
| 2 | 2   |      | [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/) |
| 3 |     |      | [155. 最小栈](https://leetcode-cn.com/problems/min-stack/)   |
| 2 | \*4 | 多次无法顺利写出 | [\**84. 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/) |
| 2 | 2   |      | [\*239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/) |

课后作业
| 敲代码 | 阅读别人代码 | 备注               | 题目                                                         |
| ------ | ------------ | -------------------- | ------------------------------------------------------------ |
| 3 |              | 软柿子 | [26. 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/) |
| 1 |              |                      | [189. 旋转数组](https://leetcode-cn.com/problems/rotate-array/) |
| 1 |              |                      | [21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/) |
| 1 | 1            | 就地合并、开额外空间 | [88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/) |
| 1 |              |               | [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)     |
| 2 | 1            | 末尾补0、交换、有变种 | [283. 移动零](https://leetcode-cn.com/problems/move-zeroes/) |
| 1 |              |  | [66. 加一](https://leetcode-cn.com/problems/plus-one/) |
| 1 |              |  | [242. 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/) |
|   |              | | [641. 设计循环双端队列](https://leetcode-cn.com/problems/design-circular-deque/) |
| 1 | \*1 | | [49. 字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/) |
| 1 |  | | [\*42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/) |

课外刷题

| 敲代码 | 阅读别人代码 | 备注                           | 题目                                                         |
| ------ | ------------ | ------------------------------ | ------------------------------------------------------------ |
| 1      | 1            | DP、DP状压                     | [120. 三角形最小路径和](https://leetcode-cn.com/problems/triangle/) |
| \*0    |              | 构造邻接表、广搜、两边同时广搜 | [\*127. 单词接龙](https://leetcode-cn.com/problems/word-ladder/) |
| 1      |              | split库函数                    | [151. 翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/) |

### week2刷题遍数记录
课内实战
| 敲代码 | 阅读别人代码 | 备注    | 题目                                                         |
| ---- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1 | \*1 | 多复习题解 | [剑指 Offer 40. 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/) |
| 这题重复 | - | - | 239. 滑动窗口最大值 |
| 这题重复 | - | - | 70. 爬楼梯 |
| 1 | 1 | 多复习 | [22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/) |
| 1 |  | 软柿子 | [226. 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/) |
| 1 |  | 软柿子 | [104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/) |
| 1 | 1 | 多复习 | [111. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/) |
| 1 | 1 | 有点意思，国际站有神仙 | [297. 二叉树的序列化与反序列化](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/) |

课后作业
| 敲代码 | 阅读别人代码 | 备注               | 题目                                                         |
| ------ | ------------ | -------------------- | ------------------------------------------------------------ |
| 1 |    |      | [590. N叉树的后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/) |
| 1 | | | [589. N叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/) |
| 1 | | 递归、迭代 | [94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) |
| 1 | | 递归、迭代 | [144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/) |
| 1 | |  | [429. N叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/) |
| 1 | 2 | 堆、3指针DP | [\*剑指 Offer 49. 丑数](https://leetcode-cn.com/problems/chou-shu-lcof/)、[\*264. 丑数 II](https://leetcode-cn.com/problems/ugly-number-ii/) |
| 1 | | | [347. 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/) |
| 2 | 2 | 多复习 | [236. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/) |
| 1 | 1 | | [105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) |
| 1 | | | [77. 组合](https://leetcode-cn.com/problems/combinations/) |
| 1 | | | [46. 全排列](https://leetcode-cn.com/problems/permutations/) |
| 1 | | | [47. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/) |

课外刷题

| 敲代码 | 阅读别人代码 | 备注                     | 题目                                                         |
| ------ | ------------ | -------------------------- | ------------------------------------------------------------ |
| 1 |    |      | [1021. 删除最外层的括号](https://leetcode-cn.com/problems/remove-outermost-parentheses/) |
| 1 | | | [103. 二叉树的锯齿形层次遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/) |
| 1 | 1 | | [1025. 除数博弈](https://leetcode-cn.com/problems/divisor-game/) |

### week3刷题遍数记录

课内实战
| 敲代码   | 阅读别人代码 | 备注           | 题目                                                         |
| -------- | ------------ | -------------- | ------------------------------------------------------------ |
| 1        |              | 软柿子         | [50. Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)    |
| 1        |              | DFS、数学      | [78. 子集](https://leetcode-cn.com/problems/subsets/)        |
| 1        |              |                | [169. 多数元素](https://leetcode-cn.com/problems/majority-element/) |
| 1        |              | 要复习         | [17. 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/) |
| 2        | 1            | 多练、用时太久 | [51. N皇后](https://leetcode-cn.com/problems/n-queens/)      |
| 2        |              |                | [102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/) |
| 1        |              |                | [433. 最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/) |
| 这题重复 |              |                | 22. 括号生成                                                 |
| 1        |              |                | [515. 在每个树行中找最大值](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/) |

课后作业

| 敲代码 | 阅读别人代码 | 备注                         | 题目                                                         |
| ------ | ------------ | ---------------------------- | ------------------------------------------------------------ |
| 1      | 1            | 有变种吧？                   | [860. 柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/) |
| 1      |              | 整个系列挺难的               | [122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/) |
| 1      |              |                              | [455. 分发饼干](https://leetcode-cn.com/problems/assign-cookies/) |
|        |              |                              | [874. 模拟行走机器人](https://leetcode-cn.com/problems/walking-robot-simulation/) |
| 2      | 4            | 重点复习                     | [127. 单词接龙](https://leetcode-cn.com/problems/word-ladder/) |
| 1      |              | 搜索、并查集                 | [200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/) |
| 1      |              | 这题不复习了，题目读半天     | [529. 扫雷游戏](https://leetcode-cn.com/problems/minesweeper/) |
| 1      |              |                              | [55. 跳跃游戏](https://leetcode-cn.com/problems/jump-game/)  |
| 2      | 2            | 多复习，二分查找的难题       | [\*33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/) |
| 1      | 1            | 二分、从右上角开始当做搜索树 | [74. 搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/) |
| 2      | 2            | 二分，多复习                 | [153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/) |
| 3      | 2            | 重点复习                     | [126. 单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii/) |
| 1      | 1            | 重点复习                     | [45. 跳跃游戏 II](https://leetcode-cn.com/problems/jump-game-ii/) |
