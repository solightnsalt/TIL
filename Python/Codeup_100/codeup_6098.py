import sys
sys.stdin = open('6098.txt')
from pprint import pprint

metrix = [list(map(int, input().split())) for _ in range(10)]
# pprint(metrix)
x, y = 1, 1
# metrix[x][y] = 9 #시작
# for i in range(9): 
#     for j in range(9):
#         if metrix[x][y+j] == 0:
#             y += j
#             metrix[x][y] = 9
#         elif metrix[x][y+j] == 1:
#             x += i
#             metrix[x][y] =9
#         else:
#             break
                                
# pprint(metrix)

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

for i in range(9):
    print(*metrix[i])

