import sys
sys.stdin = open('3009.txt')

x = []
y = []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    for i in range(3):
        if x.count(x[i]) == 1:
            xx = i
        
        elif y.count(y[i]) == 1:
            yy = i
    print(xx, yy)