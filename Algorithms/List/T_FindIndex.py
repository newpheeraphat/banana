class Solution:
    def search(self, lst : list, item : int) -> int:
        try:
            result = lst.index(item)
            return result
        except:
            return -1

if __name__ == "__main__":
    p1 = Solution()
    print(p1.search([1, 2, 3, 4], 3))
    print(p1.search([2, 4, 6, 8, 10], 8))
    print(p1.search([1, 3, 5, 7, 9], 11))
