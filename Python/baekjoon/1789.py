s = int(input())
n = 1
n_list = [1]
sum_= 1
while sum_ <= s:
    n += 1
    n_list.append(n)
    sum_ += n

if sum_ == s:
    print(len(n_list))
else:
    print(len(n_list) - 1)
    