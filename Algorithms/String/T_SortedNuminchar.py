class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s.sort(key = lambda x : x[-1:])
        res = []
        for i in s:
            res.append(i[:-1])
        return " ".join(res)
