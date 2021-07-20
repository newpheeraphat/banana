class Solution:
    def invert(self, dct : dict) -> dict:
        reverse = dict(zip(dct.values(), dct.keys()))
        return reverse

if __name__ == '__main__':
    print(Solution().invert({ "z": "q", "w": "f" }))
    print(Solution().invert({ "a": 1, "b": 2, "c": 3 }))
    print(Solution().invert({ "zebra": "koala", "horse": "camel" }))
