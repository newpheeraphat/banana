class Solution:
    def list_to_string(self, lst):
        Map = list(map(str, lst))
        return "".join(Map)

if __name__ == '__main__':
    p1 = Solution()
    print(p1.list_to_string([1, 2, 3, 4, 5, 6]))
    print(p1.list_to_string(["a", "b", "c", "d", "e", "f"]))
    print(p1.list_to_string([1, 2, 3, "a", "s", "dAAAA"]))
