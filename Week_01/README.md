# 学习笔记

切题四件套：

- 题目先理解清楚
- 先把所有解法都在脑海过一遍
- 写代码
- 测试样例

五毒神掌：

- 第一遍：五分钟读题思考，有思路就直接写，没思路就直接看题解并默写题解
- 第二遍：不看题解，自己写代码
- 第三遍：24小时后
- 第四遍：一周后
- 第五遍：面试前

## week1刷题遍数记录

有些题目因为精疲力尽了，所以就没做。

课内实战
| 敲代码 | 阅读别人代码 | 解法          | 题目                                                         |
| ---- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2   |     | 暴力、双指针  | [11. 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/) |
| 2    |     |               | [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/) |
| 2    | 1   |               | [15. 三数之和](https://leetcode-cn.com/problems/3sum/)       |
| 2    | 1   |                  | [206. 反转链表](https://leetcode-cn.com/problems/reverse-linked-list/) |
| 2    | 1   | 递归、迭代       | [24. 两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/) |
| 2    | 1   | 哈希表、快慢指针 | [141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/) |
| 1    | \*2 | 哈希表、\*快慢指针 | [\*142. 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/) |
| 1 | \*1 |                  | [25. K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/) |
| 2   | 2   |      | [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/) |
| 2    |     |      | [155. 最小栈](https://leetcode-cn.com/problems/min-stack/)   |
| 1    | \*3 |      | [\*84. 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/) |
| 1    | 2   |      | [\*239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/) |

课后作业
| 敲代码 | 阅读别人代码 | 解法                 | 题目                                                         |
| ------ | ------------ | -------------------- | ------------------------------------------------------------ |
| 2     |              |                      | [26. 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/) |
| 1      |              |                      | [189. 旋转数组](https://leetcode-cn.com/problems/rotate-array/) |
| 1      |              |                      | [21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/) |
| 1      | 1            | 就地合并、开额外空间 | [88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/) |
| 1      |              |               | [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)     |
| 2      | 1            | 末尾补0、交换 | [283. 移动零](https://leetcode-cn.com/problems/move-zeroes/) |
| 1      |              |  | [66. 加一](https://leetcode-cn.com/problems/plus-one/) |
| 1      |              |  | [242. 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/) |
|  | | | [641. 设计循环双端队列](https://leetcode-cn.com/problems/design-circular-deque/) |
| 1 | \*1 | | [49. 字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/) |
| 1 |  | | [\*42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/) |

课外刷题

| 敲代码 | 阅读别人代码 | 解法                       | 题目                                                         |
| ------ | ------------ | -------------------------- | ------------------------------------------------------------ |
| 1      | 1            | DP、DP状压                 | [120. 三角形最小路径和](https://leetcode-cn.com/problems/triangle/) |
| \*0    |              | 构造图、广搜、两边同时广搜 | [\*127. 单词接龙](https://leetcode-cn.com/problems/word-ladder/) |
| 1      |              | split库函数                | [151. 翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/) |


## 双端队列
双端队列可以理解为栈、队列的组合，所以在实际应用中可以直接使用双端队列取代栈和队列。

[Python 3 双端队列](https://docs.python.org/3/library/collections.html#collections.deque)的基本用法如下：

```python
from collections import deque
deq = deque([1, 2, 3], 3)
deq.append(4)  # [2, 3, 4]
deq.appendleft(0)  # [0, 2, 3]
deq[0]
```

[Java 8](https://docs.oracle.com/javase/8/docs/api/java/util/Deque.html) 双端队列基本用法，略。

| Python双端队列 | Head                | Tail            | Value           |
| -------------- | ------------------- | --------------- | --------------- |
| Insert         | `appendleft(value)` | `append(value)` | -               |
| Remove         | -                   | -               | `remove(value)` |
| Peek           | `deq[0]`            | `deq[-1]`       |                 |
| Remove & Peek  | `popleft()`         | `pop()`         |                 |


| Java双端队列  | Head              | Tail             | Value           |
| ------------- | ----------------- | ---------------- | --------------- |
| Insert        | `addFirst(value)` | `addLast(value)` |                 |
| Remove        | -                 | -                | `remove(value)` |
| Peek          | `peekFirst()`     | `peekLast()`     |                 |
| Remove & Peek | `removeFirst()`   | `removeLast()`   | -               |

Notes：
- Python可以插入一组 Value：`deq.extendleft([1,2])`，Java 不行
- Python可以指定 Capacity 队列最大容量，Java 不行

## 优先级队列（Priority Queue）

优先级队列只是一个应用场景，不是具体的某个数据结构，可以用 Heap、BST、Treap 来实现，一般是用 Heap。

而堆（Heap）又有各种实现，在[维基百科](https://en.wikipedia.org/wiki/Heap_(data_structure))中有一张表格列出了各种实现的性能对比。最常见/简单的实现是二叉堆，但二叉堆的性能也是最差的。

[Python3 的 heapq](https://docs.python.org/3/library/heapq.html) 是用完全二叉堆来实现的，用的时候只需要一个数组。基本用法如下。

```python
import heapq
queue = [5, 2, 1, 3]
heapq.heapify(queue)

print(queue)  # [1, 2, 5, 3]
print(queue.pop())  # 1
print(queue[0])  # 2
```

[Java 的 PriorityQueue](https://docs.oracle.com/javase/10/docs/api/java/util/PriorityQueue.html)，基本用法如下：

```java
import java.util.PriorityQueue;

public class ProorityQueueDemo {
    public static void main(String[] args) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        queue.add(5); queue.add(2); queue.add(1); queue.add(3);

        System.out.println(queue);  // [1, 3, 2, 5]
        System.out.println(queue.poll());  // 1
        System.out.println(queue.peek());  // 2
    }
}
```

|               | Python 3                       | Java 8             |
| ------------- | ------------------------------ | ------------------ |
| 建堆          | `heapq.heapify(queue)`         |                    |
| Add           | `heapq.heappush(queue, value)` | `queue.add(value)` |
| Remove & Peek | `heapq.heappop(queue)`         | `queue.poll()`     |
| Peek          | `queue[0]`                     | `queue.peek()`     |


语言差异：
- Java 建堆的时候可以通过传入比较器实现小顶堆、大顶堆等等，而 Python 建堆的时候只能建立小顶堆
- 虽然 Python 的 `nlargest()` 和 `nsmallest()` 可以传入比较器，但这两个函数比较鸡肋，只能用于离线算法不能用于在线算法

