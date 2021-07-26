class Solution:
    def frequencySort(self, s : str) -> str:
        set1 = set(s)
        dict1 = dict()
        for i in set1:
            count_all = s.count(i)
            dict1[i] = count_all
        sorted_dict1 = sorted(dict1.items(), key = lambda kv : kv[1], reverse = True)
        res = [i * j for i, j in sorted_dict1]
        return "".join(res)
