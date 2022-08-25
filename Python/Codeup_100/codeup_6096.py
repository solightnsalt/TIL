from pprint import pprint
import sys
sys.stdin = open('6096.txt')

metrix = [list(map(int, input().split())) for _ in range(19)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(19):
        if metrix[x-1][i] == 0:
            metrix[x-1][i] = 1
        else:
            metrix[x-1][i] = 0
            
    for j in range(19):
        if metrix[j][y-1] == 0:
            metrix[j][y-1] = 1
        else:
            metrix[j][y-1] = 0
            
# pprint(metrix)
for i in range(19):
    print(*metrix[i])
            
