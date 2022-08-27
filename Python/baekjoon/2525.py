h, m = map(int, input().split())
t = int(input())
a = m + t
if a < 60:
    print(h, a)
else:
    if h + (a // 60) < 24:
        print(h + (a // 60), a % 60)
    else:
        print(abs(24 - (h + (a // 60))), a % 60)