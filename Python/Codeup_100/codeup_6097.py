import sys
sys.stdin = open('6097.txt')
from pprint import pprint

h, w = map(int, input().split())
n = int(input())
metrix = [[0] * h for _ in range(w)]
# pprint(metrix)
for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0: #가로
            metrix[x-1][y-1+j] = 1
        else: #세로
            metrix[x-1+j][y-1] = 1
            
# pprint(metrix)
for i in range(h):
    print(*metrix[i])