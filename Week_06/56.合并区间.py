#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (42.82%)
# Likes:    571
# Dislikes: 0
# Total Accepted:    133.4K
# Total Submissions: 310.7K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
# 
# 
# 
# 示例 1:
# 
# 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2:
# 
# 输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
# 注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。
# 
# 
# 
# 提示：
# 
# 
# intervals[i][0] <= intervals[i][1]
# 
# 
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals = sorted(intervals, key=operator.itemgetter(0))
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[1] <= res[-1][1]:
                continue
            if interval[0] <= res[-1][1]:
                res[-1][1] = interval[1]
                continue
            res.append(interval)
        return res
# @lc code=end

