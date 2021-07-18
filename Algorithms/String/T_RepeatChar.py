string = "abc"
int1 = int(input())
result = ""
for i in range(int1):
    if len(string) < int1:
        string = string + 'a'
""" while len(str1) < int1:
    str1 = str1 + '*'
print(str1) """

print(string)
