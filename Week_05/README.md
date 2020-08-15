# 学习笔记

## 并查集

并查集元素的 key 是整数，且从 0 开始，这样就能作为下标了。疑问：要是 key 不是简单的整数该怎么办？

## 自己整理的双向BFS模板

```python
def debfs(start, end):
  if start == end:  # 必须判断
    return 2  # 根据题目 1 or 2
  s1, s2, visited = {start}, {end}, {start, end}
  level = 2  # 根据题目 1 or 2
  while s1:
    tmp = set()
    for cur in s1:
      for nex in gen_relative_nodes(cur):
        if nex in s2: return level  # found
        if nex not in visited:
          tmp.add(nex)
          visited.add(nex)
    s1 = tmp
    if len(s1) > len(s2): s1, s2 = s2, s1
  return 0  # 根据题目 0 or -1
```

## “单词搜索 II”用 Tire 树实现的时间复杂度

## 常用位运算 (背)
- `x = x & (x - 1)` 清零最低位的1

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
| 2 |              |                      | [21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/) |
| 1 | 1            | 就地合并、开额外空间 | [88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/) |
| 1 |              |               | [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)     |
| 2 | 1            | 末尾补0、交换、有变种 | [283. 移动零](https://leetcode-cn.com/problems/move-zeroes/) |
| 1 |              |  | [66. 加一](https://leetcode-cn.com/problems/plus-one/) |
| 1 |              |  | [242. 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/) |
|   |              | | [641. 设计循环双端队列](https://leetcode-cn.com/problems/design-circular-deque/) |
| 1 | \*1 | | [49. 字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/) |
| 1 |  | 重点复习 | [\*42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/) |

课外刷题

| 敲代码 | 阅读别人代码 | 备注        | 题目                                                         |
| ------ | ------------ | ----------- | ------------------------------------------------------------ |
| 1      |              | split库函数 | [151. 翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/) |

### week2刷题遍数记录
课内实战
| 敲代码 | 阅读别人代码 | 备注    | 题目                                                         |
| ---- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1 | \*1 | 多复习题解 | [剑指 Offer 40. 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/) |
| 这题重复 | - | - | 239. 滑动窗口最大值 |
| 这题重复 | - | - | 70. 爬楼梯 |
| 2 | 1 | 多复习，剪枝模板 | [22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/) |
| 1 |  | 软柿子 | [226. 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/) |
| 1 |  | 软柿子 | [104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/) |
| 2 | 3 | 多复习，易丢分，最简代码 | [111. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/) |
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
| 2 | 1 | | [46. 全排列](https://leetcode-cn.com/problems/permutations/) |
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
| 3      | 4            | 重点复习                     | [127. 单词接龙](https://leetcode-cn.com/problems/word-ladder/) |
| 1      |              | 搜索、并查集                 | [200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/) |
| 1      |              | 这题不复习了，题目读半天     | [529. 扫雷游戏](https://leetcode-cn.com/problems/minesweeper/) |
| 1      |              |                              | [55. 跳跃游戏](https://leetcode-cn.com/problems/jump-game/)  |
| 2      | 2            | 多复习，二分查找的难题       | [\*33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/) |
| 1      | 1            | 二分、从右上角开始当做搜索树 | [74. 搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/) |
| 2      | 2            | 二分，多复习                 | [153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/) |
| 3      | 2            | 重点复习                     | [126. 单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii/) |
| 1      | 1            | 重点复习                     | [45. 跳跃游戏 II](https://leetcode-cn.com/problems/jump-game-ii/) |

### week4刷题遍数记录

课内实战

| 敲代码   | 阅读别人代码 | 备注             | 题目                                                         |
| -------- | ------------ | ---------------- | ------------------------------------------------------------ |
| 1        |              |                  | [62. 不同路径](https://leetcode-cn.com/problems/unique-paths/) |
| 1        |              |                  | [63. 不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/) |
| 1        |              | 多复习           | [1143. 最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/) |
| 这题重复 |              |                  | 70. 爬楼梯                                                   |
| 1        |              | 多复习           | [120. 三角形最小路径和](https://leetcode-cn.com/problems/triangle/) |
| 1        | 1            |                  | [53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/) |
| 1        |              | 重点复习，好难啊 | [152. 乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray/) |
| 1        | 1            |                  | [322. 零钱兑换](https://leetcode-cn.com/problems/coin-change/) |
| 1        | 1            |                  | [198. 打家劫舍](https://leetcode-cn.com/problems/house-robber/) |
| 1        | 1            |                  | [213. 打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/) |
| 1        |              |                  | [121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/) |
| 这题重复 |              |                  | 122. 买卖股票的最佳时机 II                                   |
| 2        | 2            | 重点复习         | [123. 买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/) |
| 1        |              |                  | [309. 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) |
| 1        | 1            |                  | [188. 买卖股票的最佳时机 IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/) |
| 1        |              |                  | [714. 买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) |

课后作业

| 敲代码 | 阅读别人代码 | 备注               | 题目                                                         |
| ------ | ------------ | ------------------ | ------------------------------------------------------------ |
| 1      |              |                    | [64. 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/) |
| 1      |              |                    | [91. 解码方法](https://leetcode-cn.com/problems/decode-ways/) |
| 1      | \*1          |                    | [221. 最大正方形](https://leetcode-cn.com/problems/maximal-square/) |
|        |              | \*这题是不是DP啊？ | [\*621. 任务调度器](https://leetcode-cn.com/problems/task-scheduler/) |
| 1      | 1            |                    | [647. 回文子串](https://leetcode-cn.com/problems/palindromic-substrings/) |
| 1      | 1            |                    | [32. 最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/) |
| 1      |              |                    | [72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/) |
|        |              |                    | [363. 矩形区域不超过 K 的最大数值和](https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/) |
| 1      |              |                    | [403. 青蛙过河](https://leetcode-cn.com/problems/frog-jump/) |
|        |              |                    | [410. 分割数组的最大值](https://leetcode-cn.com/problems/split-array-largest-sum/) |
|        |              |                    | [552. 学生出勤记录 II](https://leetcode-cn.com/problems/student-attendance-record-ii/) |
| 1      |              |                    | [76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/) |
|        |              |                    | [312. 戳气球](https://leetcode-cn.com/problems/burst-balloons/) |

### week5

课内实战

| 敲代码 | 阅读别人代码 | 备注               | 题目                                                         |
| ------ | ------------ | ------------------ | ------------------------------------------------------------ |
| 2      | 1            | 多练，无法一气呵成 | [208. 实现 Trie (前缀树)](https://leetcode-cn.com/problems/implement-trie-prefix-tree/) |
| 1      |              | Trie               | [212. 单词搜索 II](https://leetcode-cn.com/problems/word-search-ii/) |
| 1      |              |                    | [547. 朋友圈](https://leetcode-cn.com/problems/friend-circles/) |
| 1      |              |                    | [200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/) |
| 1      |              |                    | [130. 被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/) |
| 重复   |              |                    | 70. 爬楼梯                                                   |
| 重复   |              |                    | 22. 括号生成                                                 |
|        |              | 用位运算           | [51. N皇后](https://leetcode-cn.com/problems/n-queens/)      |
| 1      | 1            |                    | [36. 有效的数独](https://leetcode-cn.com/problems/valid-sudoku/) |
| 1      | 1            | 重点复习           | [37. 解数独](https://leetcode-cn.com/problems/sudoku-solver/) |
| 重复   |              |                    | 127. 单词接龙                                                |
| 1      |              |                    | [433. 最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/) |
|        |              |                    | [1091. 二进制矩阵中的最短路径](https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/) |
|        |              |                    | [773. 滑动谜题](https://leetcode-cn.com/problems/sliding-puzzle/) |
| 1      | 1            |                    | [191. 位1的个数](https://leetcode-cn.com/problems/number-of-1-bits/) |
| 1      |              |                    | [231. 2的幂](https://leetcode-cn.com/problems/power-of-two/) |
| 1      | 1            |                    | [190. 颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits/) |
| 1      | 1            | 用位运算           | [52. N皇后 II](https://leetcode-cn.com/problems/n-queens-ii/) |
| 1      | 1            |                    | [\*338. 比特位计数](https://leetcode-cn.com/problems/counting-bits/) |

课后作业，这周作业全在课内实战里面了。
