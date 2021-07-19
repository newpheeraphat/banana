# Calculate Determinant of a 2x2 Matrix
class Solution:
    def cal_determinant(self, lst : list) -> float:
        import numpy as np 
        x = np.array(lst)
        res = np.linalg.det(x)
        return int(res)

if __name__ == '__main__':
    print(Solution().cal_determinant([[1, 2], [3, 4]]))
    print(Solution().cal_determinant([[5, 3], [3, 1]]))
