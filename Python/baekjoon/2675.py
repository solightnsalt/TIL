import sys
sys.stdin = open('2675.txt')

t = int(input())
for tc in range(t):
    r, s = input().split()
    r = int(r)
    p = []
    for i in s:
        for l in range(r):
            p.append(i)
    print(*p, sep='')