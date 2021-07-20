class Solution:
    def has_digit(self, txt : str) -> bool:
        import re
        return bool(re.search(r'\d', txt))

if __name__ == '__main__':
    print(Solution().has_digit("c8"))
    print(Solution().has_digit('23cc4'))
    print(Solution().has_digit("abwekz"))
