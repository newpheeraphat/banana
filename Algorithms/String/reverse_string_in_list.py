class Solution:
    def reverseWords(self, s: str) -> str:
        s3 = s.split()
        res = [i[::-1] for i in s3]
        return " ".join(res)
