import sys
sys.stdin = open('2851.txt')

mushroom = [int(input()) for _ in range(10)]
score = 0
for i in mushroom:
    score += i
    if score >= 100:
        if score - 100 > 100 - (score - i):
            score -= i
            break
print(score)
