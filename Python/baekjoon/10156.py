k, n, m = map(int, input().split())
a = m - (k * n)
if a < 0:
    print(abs(a))
else:
    print(0)