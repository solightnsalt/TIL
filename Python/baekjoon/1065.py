# https://www.acmicpc.net/problem/1065
n = int(input())
hansoo = 0
for i in range(1, n+1):
    # print(type(i))
    n_list = list(map(int, str(i)))
    # print(n_list) 
    if i < 100:
        hansoo += 1

    elif n_list[0] - n_list[1] == n_list[1] - n_list[2]:
        hansoo += 1

print(hansoo)      

    