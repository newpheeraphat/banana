class Solution:
    def filter_string(self, txt : str) -> list:
        count_digit = 0
        count_upper = 0
        count_special = 0 
        count_lower = 0

        for i in txt:
            if i >= 'A' and i <= 'Z':
                count_upper += 1
            elif i >= 'a' and i <= 'z':
                count_digit += 1
            elif i >= '0' and i <= '9':
                count_lower += 1
            else:
                count_special += 1
        
        return [count_upper, count_lower, count_digit, count_special]

if __name__ == '__main__':
    p1 = Solution()
    print(p1.filter_string("*$(#Mu12bas43hiR%@*!"))
    print(p1.filter_string("^^Edabit^^%$#12379"))
    print(p1.filter_string("**Airforce1**"))
