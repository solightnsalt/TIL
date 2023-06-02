# https://www.acmicpc.net/problem/2869
a, b, v = map(int, input().split())
k = (v - b) / (a - b)
if k == int(k):
    print(int(k))
else:
    print(int(k) + 1)