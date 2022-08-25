n = int(input())
sum_ = 0
p = 1
while True:
    if sum_ >= n:
        print(sum_)
        break
    else:
        sum_ += p
        p += 1
