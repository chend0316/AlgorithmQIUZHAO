# 第一遍，这题确实恶心到我了
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 问题：Python自带的sort函数直接就可以给字符串排序
        def rank_of(s):
            ret = list(s)
            ret.sort()
            return ''.join(ret)
        
        cnts = [{ 's': s, 'rank': rank_of(s) } for s in strs]
        cnts.sort(key=lambda x: x['rank'])

        res = []
        prev_rank = '#'  # 问题：对于分组问题，可以直接利用Dict的特性实现
        for cnt in cnts:
            if cnt['rank'] != prev_rank: res.append([cnt['s']])
            else: res[-1].append(cnt['s'])
            prev_rank = cnt['rank']
        
        return res

# 参考国际站，做了改进
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = ''.join(sorted(s))  # 转为原始类型才能做字典的key
            d.setdefault(key, [])
            d[key].append(s)
        return list(d.values())
