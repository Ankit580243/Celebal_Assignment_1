from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

total = list(combinations(letters, k))
count = sum(1 for combo in total if 'a' in combo)

print("{:.3f}".format(count / len(total)))
