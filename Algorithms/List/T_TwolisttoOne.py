class Solution:
    def one_list(self, lst):
        res = [y for x in lst for y in x]
        return res

if __name__ == '__main__':
    print(Solution().one_list([[1, 2], [3, 4]]))
    print(Solution().one_list([["a", "b"], ["c", "d"]]))
    print(Solution().one_list([[True, False], [False, False]]))
