class Solution:
    def convert_cartesian(self, x : list, y : list) -> list:
        res = [[i, j] for i, j in zip(x, y)]
        return res

if __name__ == '__main__':
    print(Solution().convert_cartesian([1, 5, 3, 3, 4], [5, 8, 9, 1, 0]) )
    print(Solution().convert_cartesian([9, 8, 3], [1, 1, 1]) )
