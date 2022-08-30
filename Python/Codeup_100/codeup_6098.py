import sys
sys.stdin = open('6098.txt')
from pprint import pprint

metrix = [list(map(int, input().split())) for _ in range(10)]
x, y = 1, 1

while True:
    if (metrix[x][y] == 0):
        metrix[x][y] = 9
    elif (metrix[x][y] == 2):
        metrix[x][y] = 9
        break

    if ((metrix[x][y+1] == 1 and metrix[x+1][y] == 1)):
        break

    if (metrix[x][y+1] != 1):
        y = y + 1
    elif (metrix[x+1][y] != 1):
        x = x + 1

for i in range(10):
    print(*metrix[i])

