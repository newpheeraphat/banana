string = "abc"
int1 = int(input())
result = ""
for i in range(int1):
    if len(string) < int1:
        string = string + 'a'
print(string)
