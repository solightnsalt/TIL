import sys
sys.stdin = open('5355.txt')

t = int(input())
for tc in range(t):
    cal = list(input().split())
    n = float(cal[0])
    for i in cal:
        if i == '@':
            n = n * 3
        elif i == '%':
            n = n + 5
        elif i == '#':
            n = n - 7
    print(f'{n:.2f}')