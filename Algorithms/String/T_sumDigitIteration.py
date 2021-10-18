class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        if len(num) == 1: return num
        result = sum([int(i) for i in num])
        return self.addDigits(result)
