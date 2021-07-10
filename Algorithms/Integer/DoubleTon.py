def isDoubleton(n):
    freq = set()
    for cha in str(n):
        freq.add(cha)
    return len(freq) == 2


def doubleton(n):
    while True:
        n += 1
        if isDoubleton(n):
            return n
