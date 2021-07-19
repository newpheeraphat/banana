class Solution:
    def get_frequencies(self, lst : list) -> dict:
        set1 = set(lst)
        hashmap = dict()
        for s in sorted(set1):
            count_all = lst.count(s)
            hashmap[s] = count_all
        return hashmap

if __name__ == '__main__':
    print(Solution().get_frequencies(["A", "B", "A", "A", "A"]))
    print(Solution().get_frequencies([1, 2, 3, 3, 2]))
