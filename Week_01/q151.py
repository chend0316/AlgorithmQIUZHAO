# 第一遍
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')
        res = []
        while arr:
            word = arr.pop()
            if word: res.append(word)
        return ' '.join(res)
