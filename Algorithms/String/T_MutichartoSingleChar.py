def replace(string, char):
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string)
    return string

res = replace(message, 'v')
