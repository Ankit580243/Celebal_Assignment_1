s = input().upper()
vowels = 'AEIOU'
stuart_score = 0
kevin_score = 0

for i in range(len(s)):
    if s[i] in vowels:
        kevin_score += len(s) - i
    else:
        stuart_score += len(s) - i

if kevin_score > stuart_score:
    print("Kevin", kevin_score)
elif stuart_score > kevin_score:
    print("Stuart", stuart_score)
else:
    print("Draw")