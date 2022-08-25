n = int(input())
students = list(map(int, input().split()))
q = [0] * 23
for i in students:
    q[i-1] += 1
print(*q)