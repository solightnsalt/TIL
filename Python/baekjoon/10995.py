# https://www.acmicpc.net/problem/10995

n = int(input())
for i in range(1, n + 1):
    if i % 2 == 0:
        print(' *' * n)
    else:
        print('* ' * n) 