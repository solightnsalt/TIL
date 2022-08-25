# n = 10
# k = [10, 4, 2, 3, 6, 6, 7, 9, 8, 5]
n = int(input())
k = list(map(int, input().split()))
min_ = k[0]
for i in k:
    if min_ > i:
        min_ = i
print(min_)        
