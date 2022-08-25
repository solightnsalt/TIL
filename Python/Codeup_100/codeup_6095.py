from pprint import pprint 
import sys
sys.stdin = open('6095.txt')

# 19*19 바둑판 
# n개의 흰돌

metrix = [[0] * 19 for _ in range(19)]
# print(metrix)
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    metrix[x-1][y-1] = 1
# pprint(metrix)
for i in range(19):
    print(*metrix[i])
