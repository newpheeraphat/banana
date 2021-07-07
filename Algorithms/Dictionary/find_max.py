country = ['Brazil', 'China', 'Germany', 'United States']
dict1 = {}
my_list = []
_max = 0 
for i in country:
    int1 = int(input())
    my_list.append(int1)
    dict1[i] = int1
    if _max < int1:
        _max = int1
print(dict1)
for key in dict1:
    if dict1[key] == _max:
        print(key, dict1[key])
