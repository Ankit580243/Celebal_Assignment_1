from itertools import groupby

s = input()
result = [(len(list(g)), k) for k, g in groupby(s)]
print(*result)
